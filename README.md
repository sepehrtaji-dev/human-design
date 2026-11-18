# HumanDesign

A design skill for AI coding agents. It helps an agent understand a product before choosing a visual direction, build a coherent design system, and review the result instead of falling back on the same generic UI patterns.

HumanDesign includes a reusable Agent Skill, practical design references, and optional Claude Code subagents.

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
Use human-design to design the dashboard for this project. Ask me about the visual direction before you start if anything important is unclear.
```

The skill guides the agent through product discovery, visual direction, design tokens, implementation, and visual review. It adapts to the existing stack and conventions rather than forcing a framework or component library.

## What's included

- A guided design interview and style selection process
- Design references for visual directions, color, typography, and layout
- A quality checklist for reviewing real pages and screenshots
- Three optional Claude Code subagents for research, design systems, and visual review

## Compatibility

The skill follows the open Agent Skills format. It can be used by compatible agents that support skills. The included subagent definitions use Claude Code's `.claude/agents/` format.

## License

MIT
