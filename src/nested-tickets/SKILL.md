---
name: nested-tickets
description: >
  Use when a spec needs parent tickets for Claude or Codex and small
  child tickets for Tiiny to reduce cloud token use.
---

# Nested tickets

Turn a spec, plan, or conversation into nested implementation tickets.
Prepare the work once: Tiiny completes bounded children before the
cloud agent starts their parent for integration and acceptance.

This skill authors tickets. Executor fields describe routing; the
runner or operator must honor them. Labels alone do not route agents,
verify work, retry failures, or suspend a parent.

## Gather and split

Read the spec, project instructions, tracker conventions, relevant
interfaces, and existing test commands. Reuse the project's terminology.
Resolve decisions a child would otherwise have to design before marking
its work ready. Ask only about material choices the sources cannot settle.

Make each parent a complete, observable feature slice. Give it the
`parent` label and `cloud` executor, meaning Claude or Codex. It owns
review, integration, full feature checks, and final acceptance. It lists
its children and is blocked by all of them.

Give each child the `child` label and `tiiny` executor, with exactly one
parent. Specify one testable change, its interface contract, exact paths
and symbols, a small coherent set of implementation/test files, an
artifact location, and a focused acceptance command. A child should need
little discovery or architectural judgment. Split broad tasks; do not
invent busywork to give a parent children.

Keep briefs compact by referencing exact spec sections and shared
contracts. Do not generate the implementation inside the ticket.

## Wire the dependency graph

- Containment uses `Parent` and `Children`; scheduling uses `Blocked by`.
- Every parent's blockers include every child. A child never waits on
  its own parent; that would deadlock execution.
- A child may wait on another child when it needs that artifact. A child
  needing another family's accepted feature waits on that family's
  parent. Do not depend on unaccepted work implicitly.
- Require referenced artifacts and interfaces to exist when a child
  starts. Declare shared-file ordering or another integration arrangement
  explicitly; sibling status alone does not make concurrent edits safe.
- Check that the graph is acyclic and every parent has useful children.
  Surface an unsuitable split rather than publishing a circular plan.

## Define completion and recovery

A child is complete only when its artifact exists and the runner or an
independent verifier has run its acceptance commands successfully.
Capture actual exit codes and output; a worker's success claim is not
verification. The parent then reviews the combined artifacts and runs
the feature's full acceptance checks.

Each child gets one initial Tiiny attempt and at most one correction
attempt carrying the artifact, diff, and exact failure evidence. After
that, escalate the incomplete child to the cloud executor for repair.
Record the executor override; retain its `child` relationship and leave
its parent blocked until independent checks pass. Do not create another
child with a fresh retry allowance for the same failed work.

Missing prerequisites, exhausted budgets, or unavailable execution
leave a child incomplete with a written handoff. A parent may resume
for acceptance only after all its children meet their completion gate.
Parent review can reject an artifact and reopen the affected child.

## Present and publish

Present the parent/child breakdown, executor roles, blockers, and what
each ticket delivers. Get approval unless publication is already
authorized. Follow the configured tracker; for local Markdown, use
`.scratch/<feature>/issues/<NN>-<slug>.md`, one ticket per file,
numbered in dependency order. Use the [ticket format](ticket-format.md).

Use the tracker's runnable status, normally `ready-for-agent`, for
published tickets. Blockers determine readiness; a runnable status does
not make blocked parents executable. Do not change existing source
issues or mark generated tickets complete.

Before publishing, verify reciprocal parent/child references, executor
and label fields, all blocking edges, command availability, artifact
paths, and link resolution from each ticket's directory. Report any
runner routing/verification support still needed. Stop after authoring
the tickets; do not execute their implementation work.
