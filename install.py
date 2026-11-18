#!/usr/bin/env python3
"""Install HumanDesign for supported local coding agents."""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL_SOURCE = ROOT / "skills" / "human-design"
AGENTS_SOURCE = ROOT / ".claude" / "agents"


def copy_directory(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise FileNotFoundError(f"Missing source directory: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)


def main() -> int:
    if not SKILL_SOURCE.is_dir():
        print("Could not find the HumanDesign skill files.", file=sys.stderr)
        return 1

    print("Install HumanDesign")
    print("1) Claude Code")
    print("2) Codex")
    print("3) Both")
    choice = input("Choose [1-3]: ").strip()
    home = Path.home()
    targets: list[tuple[str, Path]] = []

    if choice in {"1", "3"}:
        targets.append(("Claude Code", home / ".claude" / "skills" / "human-design"))
    if choice in {"2", "3"}:
        targets.append(("Codex", home / ".codex" / "skills" / "human-design"))
    if not targets:
        print("No valid option selected. Nothing was installed.")
        return 2

    for label, destination in targets:
        copy_directory(SKILL_SOURCE, destination)
        print(f"Installed skill for {label}: {destination}")

    if choice in {"1", "3"}:
        answer = input("Install the optional Claude Code subagents too? [Y/n]: ").strip().lower()
        if answer in {"", "y", "yes"}:
            agent_destination = home / ".claude" / "agents"
            agent_destination.mkdir(parents=True, exist_ok=True)
            for source in AGENTS_SOURCE.glob("*.md"):
                shutil.copy2(source, agent_destination / source.name)
            print(f"Installed Claude Code subagents: {agent_destination}")

    print("Done. Start a new agent session if the skill is not detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
