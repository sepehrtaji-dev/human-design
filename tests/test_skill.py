from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "human-design" / "SKILL.md"


class SkillStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL.read_text(encoding="utf-8")

    def test_agent_skill_frontmatter(self) -> None:
        match = re.match(r"^---\n(.*?)\n---\n", self.skill, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")
        frontmatter = match.group(1)
        self.assertRegex(frontmatter, r"(?m)^name: human-design$")
        description = re.search(r"(?m)^description: (.+)$", frontmatter)
        self.assertIsNotNone(description)
        self.assertLessEqual(len(description.group(1)), 1024)

    def test_all_referenced_markdown_files_exist(self) -> None:
        references = re.findall(r"\(([?:]?(?:references|examples)/[A-Za-z0-9_./-]+\.md)\)", self.skill)
        references += re.findall(r"`((?:references|examples)/[A-Za-z0-9_./-]+\.md)`", self.skill)
        self.assertTrue(references)
        for relative in references:
            with self.subTest(path=relative):
                self.assertTrue((SKILL.parent / relative).is_file())

    def test_task_paths_are_explicit_and_independent(self) -> None:
        self.assertIn("These paths are mutually exclusive starting points", self.skill)
        self.assertIn("**Audit and improve** follows the complete audit path below", self.skill)
        audit_end = self.skill.index("This is the end of the Audit and improve execution path.")
        create_workflow = self.skill.index("### 4. Understand the product")
        self.assertLess(audit_end, create_workflow)
        self.assertIn("go directly to the final report", self.skill[audit_end:create_workflow])

    def test_audit_contains_full_repair_loop(self) -> None:
        required = (
            "Establish the baseline",
            "Find design problems",
            "Prioritize findings",
            "Repair without unnecessary redesign",
            "Verify the repairs",
            "Critical",
            "Major",
            "Minor",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.skill)

    def test_review_checklist_has_measurable_contrast_and_evidence(self) -> None:
        checklist = (SKILL.parent / "references" / "review-checklist.md").read_text(encoding="utf-8")
        for phrase in ("4.5:1", "3:1", "Evidence", "Final design audit"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, checklist)

    def run_installer(self, choice: str, extra: str = "") -> tuple[subprocess.CompletedProcess[str], Path]:
        home = Path(tempfile.mkdtemp(prefix="human-design-home-"))
        env = os.environ.copy()
        env["HOME"] = str(home)
        result = subprocess.run(
            [sys.executable, str(ROOT / "install.py")],
            input=choice + "\n" + extra,
            text=True,
            capture_output=True,
            cwd=ROOT,
            env=env,
            timeout=20,
        )
        return result, home

    def test_installer_claude_code_and_optional_agents(self) -> None:
        result, home = self.run_installer("1", "y\n")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((home / ".claude/skills/human-design/SKILL.md").is_file())
        self.assertTrue((home / ".claude/agents/visual-reviewer.md").is_file())

    def test_installer_codex(self) -> None:
        result, home = self.run_installer("2")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((home / ".codex/skills/human-design/SKILL.md").is_file())
        self.assertFalse((home / ".claude/agents").exists())

    def test_installer_both_without_optional_agents(self) -> None:
        result, home = self.run_installer("3", "n\n")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((home / ".claude/skills/human-design/SKILL.md").is_file())
        self.assertTrue((home / ".codex/skills/human-design/SKILL.md").is_file())
        self.assertFalse((home / ".claude/agents").exists())

    def test_installer_rejects_invalid_choice_without_writing(self) -> None:
        result, home = self.run_installer("x")
        self.assertEqual(result.returncode, 2)
        self.assertFalse((home / ".claude").exists())
        self.assertFalse((home / ".codex").exists())


if __name__ == "__main__":
    unittest.main()
