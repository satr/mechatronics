"""Regression tests for GitHub MathJax and localized SI unit symbols."""
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from check_math_markup import math_markup_issues
from validate_repository import markdown_prose

MANIFEST = json.loads((ROOT / "tools" / "units_manifest.json").read_text(encoding="utf-8"))
LANGUAGES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))


class SIUnitParity(unittest.TestCase):
    def test_international_unit_symbols_and_local_first_use(self):
        self.assertEqual(set(LANGUAGES), set(MANIFEST["locales"]))
        self.assertEqual(len(LANGUAGES), 13)
        baseline = None
        for locale in LANGUAGES:
            with self.subTest(locale=locale):
                root = ROOT / "docs" / locale
                reference = (root / "UNITS.md").read_text(encoding="utf-8")
                self.assertIn("**" + MANIFEST["locales"][locale]["lang"] + ":**", reference.splitlines()[2])
                rows = re.findall(r"(?m)^\| \x60([^\x60]+)\x60 \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$", reference)
                self.assertEqual(len(rows), 31)
                symbols = {row[0] for row in rows}
                if baseline is None:
                    baseline = symbols
                self.assertEqual(symbols, baseline)
                for symbol, english, local, status in rows:
                    self.assertTrue(english.strip() and local.strip() and status.strip(), symbol)
                for target_locale in LANGUAGES:
                    path = "UNITS.md" if target_locale == locale else f"../{target_locale}/UNITS.md"
                    self.assertIn(f"[{target_locale}]({path})", reference)
                self.assertIn("](UNITS.md)", (root / "README.md").read_text(encoding="utf-8"))
                for relative, expected in MANIFEST["pages"].items():
                    body = (root / relative).read_text(encoding="utf-8")
                    label = MANIFEST["locales"][locale]["label"]
                    if locale == "pl":
                        # Natural Polish lessons use several grammatical forms
                        # of the unit-introduction heading; require one such
                        # heading rather than a literal phrase list.
                        present = re.findall(r"(?m)^\*\*(Jednostki[^*\n]+):\*\* ", body)
                        self.assertEqual(len(present), 1, relative)
                        label = present[0]
                    self.assertEqual(body.count(f"**{label}:**"), 1, relative)
                    prefix = body.split(f"**{label}:**", 1)[1].split("\n", 1)[0]
                    for symbol in expected:
                        self.assertIn(f"{chr(96)}{symbol}{chr(96)} — ", prefix, relative)
                    link = "../UNITS.md" if relative.startswith("notes/") else "UNITS.md"
                    self.assertIn(f"]({link})", prefix)
                    self.assertLess(body.index(f"**{label}:**"), body.find("## ", 5)
                                    if "## " in body else len(body))

    def test_si_percent_spacing_and_degree_exception(self):
        for locale in LANGUAGES:
            for page in (ROOT / "docs" / locale).rglob("*.md"):
                with self.subTest(page=str(page.relative_to(ROOT))):
                    prose = markdown_prose(page.read_text(encoding="utf-8"))
                    self.assertNotRegex(prose, r"\d+(?:\.\d+)?%(?![0-9A-Fa-f]{2})")
                    self.assertNotRegex(prose, r"\d+(?:\.\d+)?\\%(?![0-9A-Fa-f]{2})")
            unit_ref = (ROOT / "docs" / locale / "UNITS.md").read_text(encoding="utf-8")
            self.assertIn("1° = π/180 rad", unit_ref)
            self.assertIn("1 rpm = 2π/60 rad/s", unit_ref)

    def test_all_math_source_delimiters_and_tex_groups(self):
        pages = [page for loc in LANGUAGES for page in (ROOT / "docs" / loc).rglob("*.md")]
        self.assertGreaterEqual(len(pages), 200)
        for path in pages:
            with self.subTest(path=str(path.relative_to(ROOT))):
                issues = math_markup_issues(path.read_text(encoding="utf-8"))
                self.assertEqual(issues, [], f"{path}: {issues[:8]}")

    def test_velocity_is_italic_variable_not_upright_unit_symbol(self):
        # v_x and v_y are physical variables; \mathrm is reserved for
        # upright unit symbols and descriptive subscripts.
        for locale in LANGUAGES:
            body = (ROOT / "docs" / locale / "notes" / "05-velocity-jacobian.md").read_text(encoding="utf-8")
            self.assertNotIn(r"\mathrm{v}", body)
            self.assertIn(r"v_x=", body)
            self.assertIn(r"v_y=", body)

    def test_detects_malformed_math_without_execution(self):
        samples = (
            ("Ratio $\\frac{1}{2.", "unpaired inline math dollar"),
            ("$$\n\\frac{1}{2\n$$", "Unbalanced TeX braces"),
            ("$$\nx=\\left(2\n$$", "Mismatched TeX"),
            ("$$\\frac{1}{2}$$", "must be on separate lines"),
        )
        for source, expected in samples:
            with self.subTest(source=source):
                self.assertIn(expected, " ".join(math_markup_issues(source)))


if __name__ == "__main__":
    unittest.main()
