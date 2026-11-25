# Local ticket format

Use the project's existing tracker fields and statuses. Add the role and
relationship fields below. These fields are a contract for the runner
or operator; they do not add runtime behavior to an existing tracker.

Parent tickets carry:

- `Labels: parent` and `Executor: cloud`.
- `Children`: every associated child ID with a sibling Markdown link.
- `Blocked by`: every child ID plus genuine external prerequisites.
- `Touches`, the feature's observable outcome, and full acceptance checks.

Child tickets carry:

- `Labels: child` and `Executor: tiiny`.
- `Parent`: exactly one parent ID with a sibling Markdown link.
- `Blocked by`: actual prerequisites, excluding their own parent.
- `Touches`, the interface contract, and the bounded deliverable.
- `Artifact`: a diff/commit or output path with a written handoff.
- `Acceptance command`: an exact focused check, run independently.
- `Failure policy`: one correction, then cloud repair of the same child.

Render fields as `**Field:** value`, matching ordinary local tickets.
Use the full filename as a link target relative to the ticket directory.
Numeric dependency IDs follow the tracker's `Blocked by` convention.
For another feature, use its supported qualified ticket identifiers.

## Example family

This miniature example assumes a project with the named Vitest command
and an agreed `encodeRows(rows:string[][]):string` CSV contract. Actual
tickets must include the exact semantics settled in their own spec.

File `01-encode-csv.md`:

```markdown
# 01: Implement CSV escaping

**Labels:** child
**Executor:** tiiny
**Parent:** [02](02-accept-csv.md)
**Blocked by:** None
**Touches:** src/export/csv.ts, test/csv.spec.ts
**Status:** ready-for-agent

**What to build:** Implement encodeRows using the agreed CSV contract.
Quote cells containing commas, double quotes, CR, or LF; double embedded
quotes. Preserve cell and row order and leave inputs unchanged.

**Artifact:** Reviewable diff and .scratch/csv/artifacts/01-report.md
with changed paths, check output, exit codes, and unresolved issues.
**Acceptance command:** npx vitest run test/csv.spec.ts
**Failure policy:** One Tiiny correction, then cloud repair of this
child. Keep it incomplete until independent checks pass.

- [ ] Exact expected outputs cover escaping and ordinary cells.
- [ ] Independent execution of the focused tests passes.
```

File `02-accept-csv.md`:

```markdown
# 02: Accept the CSV encoder

**Labels:** parent
**Executor:** cloud
**Children:** [01](01-encode-csv.md)
**Blocked by:** 01
**Touches:** src/export/csv.ts, test/csv.spec.ts
**Status:** ready-for-agent

**What to build:** Accept a reusable encoder meeting the CSV contract.

- [ ] Review child 01's actual diff and independent check evidence.
- [ ] Verify the full CSV contract and meaningful test assertions.
- [ ] Run the project's full acceptance checks and record results.
```

A later UI child's `Blocked by: 02` waits for the accepted encoder.
Its own parent lists that UI child under both `Children` and `Blocked by`.
No child waits on its own parent. On escalation, retain the child's
identity and parent link while recording `Executor: cloud` for repair.
