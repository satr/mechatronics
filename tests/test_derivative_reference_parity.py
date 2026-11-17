"""Strict 12-locale derivative reference parity and numerical checks.

These assertions compare equations, domain symbols and navigability; they do
not constitute native-speaker proofreading or proof of translation quality.
"""
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))
REFERENCE = "DERIVATIVE_TABLE.md"


def table_rows(body):
    rows = [line for line in body.splitlines() if line.startswith("|")]
    if len(rows) != 23:
        raise AssertionError(f"Expected header, separator and 21 derivative rows, got {len(rows)}")
    return [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in rows]


def displayed_math(body):
    return re.findall(r"(?ms)^\$\$\n(.*?)\n\$\$$", body)


class DerivativeReferenceParity(unittest.TestCase):
    def test_all_locales_have_same_formulas_domains_examples_and_navigation(self):
        english = (ROOT / "docs" / "en" / REFERENCE).read_text(encoding="utf-8")
        canonical_rows = table_rows(english)
        canonical_display = displayed_math(english)
        self.assertEqual(len(canonical_display), 3)
        self.assertEqual(len(canonical_rows), 23)
        self.assertEqual(len(LOCALES), 13)
        for locale in LOCALES:
            with self.subTest(locale=locale):
                path = ROOT / "docs" / locale / REFERENCE
                body = path.read_text(encoding="utf-8")
                rows = table_rows(body)
                for number, (actual, canonical) in enumerate(zip(rows[2:], canonical_rows[2:]), 1):
                    self.assertEqual(actual[:2], canonical[:2], (locale, number))
                    # Conditions are translated, but their mathematical domain
                    # symbols and inequalities may not silently disappear.
                    self.assertEqual(
                        re.findall(r"\$([^$]*)\$", actual[2]),
                        re.findall(r"\$([^$]*)\$", canonical[2]),
                        (locale, number),
                    )
                self.assertTrue(set(canonical_display).issubset(set(displayed_math(body))))
                for term in (
                    r"u'=\frac{\mathrm{d}u}{\mathrm{d}x}",
                    r"v'=\frac{\mathrm{d}v}{\mathrm{d}x}",
                    r"y=(3x^2+1)^4",
                    r"x(t)=2\ \mathrm{mm}+(3\ \mathrm{mm/s})t+(2\ \mathrm{mm/s^2})t^2",
                    r"f'(y)\ne0",
                    r"(f^{-1})'(x)=1/f'(y)",
                    r"11\ \mathrm{mm/s}",
                ):
                    self.assertIn(term, body)
                # Each edition has a reciprocal same-page switcher for all
                # supported language directories, including itself.
                selector = body.splitlines()[2]
                for other in LOCALES:
                    destination = REFERENCE if other == locale else f"../{other}/{REFERENCE}"
                    self.assertIn(f"[{other}]({destination})", selector)
                self.assertIn(f"]({REFERENCE})",
                              (ROOT / "docs" / locale / "README.md").read_text(encoding="utf-8"))
                # The page itself needs localized links to its own index,
                # integral reference and foundations, not just a selector.
                for local_target in ("README.md", "INTEGRAL_TABLE.md",
                                     "notes/00-calculus-foundations.md"):
                    self.assertIn(f"]({local_target})", body)
                if locale not in ("en", "fi", "ko"):
                    # Previous mechanical rewrite accidentally duplicated
                    # the velocity heading; keep exactly one bold pair.
                    example_line = next(line for line in body.splitlines()
                                        if line.startswith("**") and
                                        r"x(t)=2\ \mathrm{mm}" in line)
                    self.assertEqual(example_line.count("**"), 2)
                self.assertNotIn("translation in progress", body.lower())

    def test_original_english_placeholder_prose_is_gone_from_translations(self):
        for locale in set(LOCALES) - {"en"}:
            with self.subTest(locale=locale):
                body = (ROOT / "docs" / locale / REFERENCE).read_text(encoding="utf-8")
                for untranslated in (
                    "The derivative is defined where the relevant limit exists.",
                    "For composite functions use the chain rule.",
                    "**Chain rule:** For",
                    "**Inverse functions:** If",
                    "With $x(t)=",
                    "At $t=2",
                    "real $n$; where defined and differentiable",
                    "| product rule |",
                    "| chain rule |",
                    "[Course index](README.md)",
                ):
                    self.assertNotIn(untranslated, body)

    def test_independent_worked_result_checks(self):
        # x(t)=2+3t+2t² mm; differentiate in the time variable.
        t = 2.0
        position = 2.0 + 3.0 * t + 2.0 * t * t
        velocity = 3.0 + 4.0 * t
        acceleration = 4.0
        self.assertEqual(position, 16.0)
        self.assertEqual(velocity, 11.0)
        self.assertEqual(acceleration, 4.0)
        # d/dx (3x²+1)^4 = 24x(3x²+1)^3 by the chain rule.
        x, dt = 1.0, 1e-6
        y = lambda value: (3 * value * value + 1) ** 4
        numerical = (y(x + dt) - y(x - dt)) / (2 * dt)
        algebraic = 24 * x * (3 * x * x + 1) ** 3
        self.assertTrue(math.isclose(numerical, algebraic, rel_tol=1e-10))


if __name__ == "__main__":
    unittest.main()
