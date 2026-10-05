from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "references/architecture.md",
    "references/design-system.md",
    "references/qa-checklist.md",
    "references/tool-routing.md",
    "templates/project-brief.md",
    "templates/page-map.md",
    "templates/revision-log.md",
    "plugin-ready/README.md",
    "plugin-ready/tool-contracts.yaml",
    "scripts/validate_skill.py",
]

REQUIRED_SKILL_TERMS = [
    "Use when",
    "No Silent Fallback",
    "Page Map",
    "Thai QA",
    "Visual QA",
    "PDF Preflight",
    "Human Approval",
    "A4",
    "image generation",
    "Adobe",
]

class SkillContractTests(unittest.TestCase):
    def test_required_package_files_exist(self):
        missing = [p for p in REQUIRED_FILES if not (ROOT / p).exists()]
        self.assertEqual(missing, [], f"Missing required files: {missing}")

    def test_skill_frontmatter_and_name(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertRegex(text, r"(?m)^name:\s*designing-pdf-manuals\s*$")
        self.assertRegex(text, r"(?m)^description:\s*Use when .+")

    def test_skill_contains_required_workflow_gates(self):
        text = SKILL.read_text(encoding="utf-8")
        missing = [t for t in REQUIRED_SKILL_TERMS if t not in text]
        self.assertEqual(missing, [], f"Missing required skill terms: {missing}")

    def test_skill_has_ordered_core_phases(self):
        text = SKILL.read_text(encoding="utf-8")
        phases = [
            "Intake", "Analyze", "Page Map", "Research / Assets", "Write",
            "Image / Diagram", "Layout", "Thai QA", "Visual QA",
            "PDF Preflight", "Human Approval", "Release"
        ]
        positions = [text.find(p) for p in phases]
        self.assertTrue(all(p >= 0 for p in positions), positions)
        self.assertEqual(positions, sorted(positions), positions)

    def test_skill_is_concise(self):
        words = SKILL.read_text(encoding="utf-8").split()
        self.assertLessEqual(len(words), 500, f"SKILL.md too long: {len(words)} words")

    def test_no_placeholders_in_shipped_docs(self):
        bad = []
        for path in ROOT.rglob("*.md"):
            if "tests" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            if re.search(r"\b(TBD|TODO)\b", text):
                bad.append(str(path.relative_to(ROOT)))
        self.assertEqual(bad, [], f"Placeholders found in: {bad}")

if __name__ == "__main__":
    unittest.main()
