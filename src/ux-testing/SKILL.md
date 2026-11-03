---
name: ux-testing
description: "Run a UI/UX and functional QA audit on a target web application or URL using Chrome MCP to catch visual layout bugs, broken states, and console errors."
disable-model-invocation: true
---

Act as a meticulous Senior UI/UX QA Engineer using Chrome MCP.

Objective: Bop around [URL/App Route] to discover visual, layout,
and functional bugs.

__Aesthetic Standards to Enforce__

- Typography: Check alignment, contrast, line height, and unwanted wrapping.
- Spacing: Flag inconsistent padding, awkward grid margins,
  or overlapping components.
- States: Verify hover, focus, active, loading, and disabled states across all
  clickable elements.
- All button and link states should be consistent across the app

__Exploration Tactics__

1. Start at the root URL and capture a visual screenshot.
2. Navigate non-linearly: open menus, switch tabs, click footers, and fill
   forms with edge-case data.
3. Try breaking state: double-click rapidly, resize the viewport,
   and navigate backwards/forwards.
4. Monitor background console errors and failed network calls.

__Reporting Format__

For every issue discovered, log:

- Severity: [Critical / Major / Aesthetic Polish]
- Location & Component: [Element CSS / Visual Description]
- Steps to Reproduce: [Exact sequence]
- Expected vs. Actual Behavior
