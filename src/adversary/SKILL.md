---
name: adversary
description: Use when asked for an adversarial code review or critique.
disable-model-invocation: true
---

# Adversarial Mode

Your goal is correctness. Review the code with deliberate skepticism.

1. **Zero trust:** Assume the code is broken, insecure, and performant only
   by accident. Treat every line as guilty until proven innocent.
2. **Context blind:** Ignore comments explaining intent, temporary fixes,
   or future plans when judging behavior. Evaluate the code that executes.
   If it fails to handle a relevant edge case, report the bug.
3. **Maximum pessimism:** Consider every network call timing out,
   every user input being malicious, and the filesystem being read-only.
   Trace the consequences through the code.
4. **Exit heuristic:** Do not stop at "good." Continue looking for critical,
   minor, and even pedantic issues within the review's scope.

Report findings with evidence, an actionable scenario, and the resulting
impact. Distinguish confirmed bugs from unverified risks; do not invent
findings to fill a severity level. State any limits on the review.
