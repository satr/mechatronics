"""Prevent accidental duplication of the long canonical maintenance guide."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MaintenanceDocumentStructure(unittest.TestCase):
    def test_single_document_title_and_unique_major_sections(self):
        text = (ROOT / "MAINTENANCE.md").read_text(encoding="utf-8")
        self.assertEqual(text.count("# Maintaining and extending this curriculum"), 1)
        sections = re.findall(r"^## .+$", text, flags=re.MULTILINE)
        self.assertEqual(len(sections), len(set(sections)))
        for section in ("## Learning path and scope",
                        "## tf2 versus URDF/state-source semantics",
                        "## Mathematical notation and executable examples",
                        "## Local Python only",
                        "## Basic calculus course and reference"):
            self.assertEqual(sections.count(section), 1)

    def test_important_recent_guidance_is_not_lost(self):
        text = (ROOT / "MAINTENANCE.md").read_text(encoding="utf-8")
        for phrase in ("Keep the worked W → T → S composition",
                       "Within Markdown math delimiters",
                       "For the first-order response in calculus chapter 00",
                       "The optional local Jupyter notebooks are executable artifacts too"):
            self.assertEqual(text.count(phrase), 1)


if __name__ == "__main__":
    unittest.main()
