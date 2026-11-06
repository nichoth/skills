#!/usr/bin/env python3
"""Cross-process advisory file locking for the review worktree cache.

`resolve_branches.py` can run concurrently: several review agents, or a
user invoking it while a review is already in flight. Each run mutates a
shared worktree root, so the mutating sections are serialized with an
exclusive `flock` on a sentinel file inside that root.

The lock is advisory. It only excludes processes that take the same lock,
so external writers touching the worktree cache are not held off.
"""

import errno
import os
import time

try:
    import fcntl
    HAS_FCNTL = True
except ImportError:  # platforms without fcntl, e.g. Windows
    fcntl = None
    HAS_FCNTL = False

# The guarded section runs `git fetch` against every remote plus a
# `git worktree add`, so a legitimate holder can be slow. This bounds a
# stuck lock rather than pacing a healthy one.
DEFAULT_TIMEOUT = 300.0
POLL_INTERVAL = 0.1


class LockTimeout(TimeoutError):
    """Raised when the lock is not acquired within the timeout."""


class FileLock:
    """Exclusive advisory lock held for the duration of a `with` block.

    The lock file is created when absent and deliberately left on disk
    afterwards. Unlinking it on release would let a second process create
    and lock a fresh inode while the first still holds the old one, so
    both would believe they hold the lock.
    """

    def __init__(self, path, timeout=DEFAULT_TIMEOUT):
        if not HAS_FCNTL:
            raise RuntimeError(
                "fcntl is required for file locking; this script supports "
                "macOS and Linux only."
            )
        self.path = path
        self.timeout = timeout
        self._fd = None

    def acquire(self):
        if self._fd is not None:
            raise RuntimeError(f"Lock is already held: {self.path}")

        parent = os.path.dirname(os.path.abspath(self.path))
        if parent:
            os.makedirs(parent, exist_ok=True)

        fd = os.open(self.path, os.O_RDWR | os.O_CREAT | os.O_CLOEXEC, 0o644)
        deadline = time.monotonic() + self.timeout
        try:
            while True:
                try:
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except OSError as e:
                    if e.errno not in (errno.EACCES, errno.EAGAIN):
                        raise
                    if time.monotonic() >= deadline:
                        raise LockTimeout(
                            f"Timed out after {self.timeout:g}s waiting for "
                            f"lock: {self.path}"
                        )
                    time.sleep(POLL_INTERVAL)
        except BaseException:
            os.close(fd)
            raise

        self._fd = fd
        # Breadcrumb for diagnosing a stuck lock. Best effort: failing to
        # record the owner is not a reason to fail an acquired lock.
        try:
            os.ftruncate(fd, 0)
            os.write(fd, f"{os.getpid()}\n".encode("utf-8"))
        except OSError:
            pass
        return self

    def release(self):
        if self._fd is None:
            return
        fd, self._fd = self._fd, None
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)

    def __enter__(self):
        return self.acquire()

    def __exit__(self, exc_type, exc, tb):
        self.release()
        return False
