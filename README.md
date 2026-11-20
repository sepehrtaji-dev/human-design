# HumanDesign

A design skill for AI coding agents. It helps an agent understand a product before choosing a visual direction, build a coherent design system, and improve existing interfaces by finding and fixing real design problems.

HumanDesign includes a reusable Agent Skill, practical design references, a Design DNA template, and optional Claude Code subagents.

## Install

Clone or download this repository, then run:

```bash
python install.py
```

Choose Claude Code or Codex. The installer copies the skill into your user-level skills directory. For Claude Code, it can also install the three optional subagents.

You can also install it manually by copying `skills/human-design` into:

- Claude Code: `~/.claude/skills/human-design`
- Codex: `~/.codex/skills/human-design`

Claude Code subagents are installed separately into `~/.claude/agents/`.

## Use

Start a design task and ask your agent to use `human-design`. For example:

```text
Use human-design to audit this dashboard, find what makes the current design feel inconsistent and unfinished, and fix the issues without changing its overall identity.
```

For a new interface, you can ask the agent to design a page and establish its visual direction. For an existing interface, it can inspect the current implementation, prioritize design problems, make focused repairs, and verify the result.

For projects with multiple pages, HumanDesign can create a `design/DESIGN-DNA.md` file to keep visual decisions consistent across future work.

## What's included

- A guided product and visual-direction workflow
- An existing-design audit and repair workflow
- Design references for visual directions, color, typography, and layout
- A Design DNA guide and starter template
- A quality checklist for reviewing real pages and screenshots
- Three optional Claude Code subagents for research, design systems, and visual review

## Validate

Run the local checks with:

```bash
python -m unittest discover -s tests -v
```

The suite checks the skill structure and references, keeps the task paths separate, and exercises the installer for Claude Code, Codex, both targets, and invalid input in temporary home directories. GitHub Actions runs the same checks on pushes and pull requests.

## Compatibility

The skill follows the open Agent Skills format. It can be used by compatible agents that support skills. The included subagent definitions use Claude Code's `.claude/agents/` format.

## License

MIT
