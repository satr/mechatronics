"""Check localized finite-difference precision warnings are not omitted.

This structural check is not a proof of translation semantic equivalence.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class FiniteDifferencePrecisionParity(unittest.TestCase):
    def test_warning_appears_in_derivative_section_of_every_locale(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        self.assertTrue(locales)
        for locale in locales:
            with self.subTest(locale=locale):
                source = (ROOT / "docs" / locale / "notes" /
                          "01-motion-calculus.md").read_text(encoding="utf-8")
                start, end = '<a id="section-2"></a>', '<a id="section-3"></a>'
                self.assertEqual(source.count(start), 1)
                self.assertEqual(source.count(end), 1)
                section = source.split(start, 1)[1].split(end, 1)[0]
                for literal in ("1e-17", "ValueError", "forward_derivative",
                                "01_motion_and_integral.py", r"4\ \mathrm{mm/s}"):
                    self.assertIn(literal, section)


if __name__ == "__main__":
    unittest.main()
