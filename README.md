# skills

Skills for the machines.

Install with `npx skills`.

<details><summary><h2>Contents</h2></summary>

<!-- toc -->

- [Corvidae-Coding-Projects/real-testing](#corvidae-coding-projectsreal-testing)
  * [Install](#install)
- [Prop Testing](#prop-testing)
  * [Install](#install-1)
- [Adversarial Review](#adversarial-review)
  * [Install](#install-2)
- [UX Testing](#ux-testing)
  * [Install](#install-3)
- [See Also](#see-also)

<!-- tocstop -->

</details>

## Corvidae-Coding-Projects/real-testing

### Install

```sh
npx skills add https://github.com/Corvidae-Coding-Projects/Project-Peritus/tree/main/skills/real-testing
```

---

## Prop Testing

Forked from [inanna-malick/agent-skills](https://github.com/inanna-malick/agent-skills/blob/ee03a7bcc316dfbaed56cfda16006ac10840d78a/skills/proptest-praxis/SKILL.md).

* Remove some Rust-specific parts
* convert to `npm` package manager
* use `fast-check`, because Typescript
* disable model-invocation

```yaml
name: proptest
description: >
  Build model-based property-testing suites to find correctness bugs,
  then reduce failures to deterministic regression tests and minimal fixes.
  Use for broad property-testing coverage of custom data structures and
  algorithms, including operation-sequence generators and independent
  reference models.
disable-model-invocation: true
```

### Install

```sh
npx skills add nichoth/skills --skill proptest -a claude-code -a universal
```

---

## Adversarial Review

```yaml
---
name: adversarial-review
description: >
  Adversarial review of two git worktrees to find bugs/quality issues before
  merge. Do not use for simple diffs or neutral walkthroughs.
disable-model-invocation: true
---
```

### Install

```sh
npx skills add nichoth/skills --skill adversarial-review -a claude-code -a universal
```


## UX Testing

See [SKILL.md](src/ux-testing/SKILL.md).

```yaml
---
name: ux-testing
description: >
  Run a UI/UX and functional QA audit on a target web application or URL using
  Chrome MCP to catch visual layout bugs, broken states, and console errors.
disable-model-invocation: true
---
```

### Install

From the repo that consumes this:

```sh
npx skills add nichoth/skills --skill ux-testing -a claude-code -a universal
```

That will install the skill as a dependency. The `-a` flag is for agent.
`-a claude-code` installs skills in `.claude/skills/`, `-a universal` installs
them in `.agents/skills/`. 


## See Also

* ["description" in frontmatter is the trigger](https://youtu.be/5Bmp9cz1JN8?t=261)
  (This is only relevant in skills where `disable-model-invocation` is false.)
* [Corvidae-Coding-Projects/real-testing](https://github.com/Corvidae-Coding-Projects/Project-Peritus/tree/9af00845b71a4ee793ecc2f9b5d05adb749a009d/skills/real-testing)
