"""Check first-order initial-condition reasoning in all calculus translations.

The numerical assertion is independent of the tutorial text. This structural
test does not establish full semantic or native-language translation quality.
"""
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class FirstOrderInitialConditionTranslationParity(unittest.TestCase):
    def test_nonzero_initial_speed_response_matches_exponential(self):
        expected = 1000 + (200 - 1000) * math.exp(-1)
        self.assertAlmostEqual(expected, 705.6964470628461, places=8)
        self.assertAlmostEqual((expected - 200) / (1000 - 200),
                               1 - math.exp(-1), places=12)

    def test_all_editions_have_assumption_general_formula_and_worked_example(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        self.assertTrue(locales)
        general = r"\omega(t)=\omega_\infty+(\omega_0-\omega_\infty)\exp(-t/\tau)."
        worked = r"\omega(\tau)=1000+(200-1000)\exp(-1)\approx705.7\ \mathrm{rpm}."
        for locale in locales:
            with self.subTest(locale=locale):
                source = (ROOT / "docs" / locale / "notes" /
                          "00-calculus-foundations.md").read_text(encoding="utf-8")
                start, end = '<a id="section-5"></a>', '<a id="section-6"></a>'
                self.assertEqual(source.count(start), 1)
                self.assertEqual(source.count(end), 1)
                section = source.split(start, 1)[1].split(end, 1)[0]
                for token in (r"\omega(0)=0", r"\omega_0", r"\omega_\infty",
                              general, worked, "200", "800", "1000", "0.5"):
                    self.assertIn(token, section)
                self.assertNotIn("\n$\n", section)
                self.assertEqual(sum(line.strip() == "$$"
                                     for line in section.splitlines()) % 2, 0)


if __name__ == "__main__":
    unittest.main()
