"""Catch escaped TeX command strings in translated calculus-table math.

The Markdown *file* must contain one literal backslash before each TeX
command, even when external APIs serialize it using additional escapes.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CalculusTableTexSyntax(unittest.TestCase):
    def test_integral_math_is_real_tex_in_every_locale(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        self.assertTrue(locales)
        expected = (r"$\int v\ \mathrm{d}t$", r"$\int F\ \mathrm{d}x$")
        damaged = (r"$\\int v\\ \\mathrm{d}t$", r"$\\int F\\ \\mathrm{d}x$")
        for locale in locales:
            with self.subTest(locale=locale):
                doc = (ROOT / "docs" / locale / "notes" / "00-calculus-foundations.md")
                text = doc.read_text(encoding="utf-8")
                start, end = '<a id="section-1"></a>', '<a id="section-2"></a>'
                self.assertEqual(text.count(start), 1)
                self.assertEqual(text.count(end), 1)
                table = text.split(start, 1)[1].split(end, 1)[0]
                for good, bad in zip(expected, damaged):
                    self.assertIn(good, table)
                    self.assertNotIn(bad, table)


if __name__ == "__main__":
    unittest.main()
