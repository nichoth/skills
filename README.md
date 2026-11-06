# skills

Skills for the machines.

Install with `npx skills`.

<details><summary><h2>Contents</h2></summary>

<!-- toc -->

- [UX Testing](#ux-testing)
  * [Install](#install)
- [See Also](#see-also)

<!-- tocstop -->

</details>

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
npx skills add nichoth/skills --skill ux-testing -a claude-code -a universal
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
