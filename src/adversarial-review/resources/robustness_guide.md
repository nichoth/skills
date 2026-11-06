# Git Diff Robustness Guide

This guide details best practices and compatibility standards for
safely extracting, paging, and parsing git diffs.

## 1. Tooling Contract
- **Primary Viewer**: The `Read` tool is the primary file viewer. It takes
  an absolute path, an `offset` (the 1-indexed line to start from) and a
  `limit` (how many lines to return), and echoes results in `cat -n`
  form. Absent a `limit` it returns up to 2000 lines.
- **Fallback**: If `Read` is unavailable, fall back to shell commands such
  as `sed -n '<start>,<end>p' "<file_path>"` or `head`/`tail`.
- Do not use `cat` or interactive pagers (e.g. `less`).

## 2. Directory Creation & Quoting
- Always ensure the target scratch directory exists before executing
  redirections:
  `mkdir -p "<scratch-dir>"`.
- Quote all shell paths and parameters in commands to handle paths
  containing spaces or special characters.

## 3. Temporary File Roles
- `temp_diff_stat.txt`: Stores changed-file statistics.
- `temp_diff_all.txt`: Stores complete diff hunks and context.
- `temp_diff_paths.txt`: Stores null-delimited name-status list.

## 4. Special Git Cases
- **Renames & Modes**: Explicitly check diff headers for renames
  (`rename from ...`), mode changes (`old mode ... new mode`), and
  binary files (`Binary files ... differ`).
- **Binary Files**: Report binary changes in the summary, but omit
  detailed text diffs.

## 5. Pagination & EOF Detection
- To prevent terminal truncation, read files in successive, chunked lines.
- Do not rely on receiving a short chunk as an EOF signal. Instead,
  calculate the total line count beforehand (e.g. check if the file
  lacks a trailing newline character and increment by 1). Read
  iteratively until `offset` exceeds this logical line count.

## 6. Cleanup
- **Prohibited Deletions**: Never delete repository-tracked files,
  worktree-tracked files, unknown paths, or perform broad recursive
  paths/deletions. Never run deletions inside the repository or
  worktree.
- **Allowed Deletions (Exception)**: Exact, agent-created temporary
  files and directories under the verified conversation scratch
  directory (e.g. `<scratch-dir>/`)
  are an explicit exception and can be safely deleted, even when
  `<scratch-dir>` resides beneath the cloned configuration repository
  path.
- **Safe Commands**: Use `rm -- <known-file>` and
  `rmdir <known-empty-directory>` for cleanup (`rm -- <known-file>`
  remains the default for one-shot deletions, but signal/EXIT trap
  handlers MUST use `rm -f -- <known-file>` because they are
  re-entrant and must be idempotent). Never use `rm -rf` in any
  context. If an OS temporary directory was created via
  `TEMP_DIR=$(mktemp -d)`, delete only the specific temporary files
  inside it, then remove the empty directory with
  `rmdir -- "$TEMP_DIR"`.
