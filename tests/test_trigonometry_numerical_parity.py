"""Numerical check of all localized unit-circle tables and inverse quadrants.

Read Markdown as data, not executable expressions.
"""
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANGLES = (0, 30, 45, 60, 90, 120, 135, 150,
          180, 210, 225, 240, 270, 300, 315, 330)
ARCTAN_CELL = re.compile(r"^\$(-?\d+)\^\\circ\$$")


def table_rows(text):
    lines = text.splitlines()
    starts = [n for n, line in enumerate(lines) if line.startswith("| θ |")]
    if len(starts) != 1:
        raise ValueError("Expected one trigonometric reference table")
    rows = []
    for line in lines[starts[0] + 2:]:
        if not line.startswith("|"):
            break
        rows.append([part.strip() for part in line.strip().strip("|").split("|")])
    return rows


class TrigonometryNumericalParity(unittest.TestCase):
    def test_all_table_values_and_principal_inverse_angles(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        self.assertTrue(locales)
        for locale in locales:
            with self.subTest(locale=locale):
                text = (ROOT / "docs" / locale / "TRIGONOMETRY.md").read_text(
                    encoding="utf-8")
                rows = table_rows(text)
                self.assertEqual(len(rows), len(ANGLES))
                for degrees, cells in zip(ANGLES, rows):
                    with self.subTest(locale=locale, degrees=degrees):
                        self.assertEqual(len(cells), 8)
                        self.assertEqual(cells[0], f"{degrees}°")
                        angle = math.radians(degrees)
                        for index, value in ((2, math.cos(angle)),
                                             (4, math.sin(angle))):
                            self.assertAlmostEqual(float(cells[index]),
                                                   value, delta=0.000051)
                        if degrees in (90, 270):
                            self.assertRegex(cells[5], r"^\*\*[^*]+\*\*$")
                            self.assertEqual(cells[6], "—")
                            self.assertEqual(cells[7], "—")
                        else:
                            self.assertAlmostEqual(float(cells[6]),
                                                   math.tan(angle),
                                                   delta=0.000051)
                            m = ARCTAN_CELL.fullmatch(cells[7])
                            self.assertIsNotNone(m)
                            principal = math.degrees(math.atan(math.tan(angle)))
                            self.assertAlmostEqual(int(m.group(1)), principal,
                                                   delta=0.000001)

    def test_inverse_direction_requires_both_signs(self):
        self.assertAlmostEqual(math.degrees(math.atan(1 / -1)), -45)
        self.assertAlmostEqual(math.degrees(math.atan2(1, -1)), 135)
        self.assertAlmostEqual(math.degrees(math.atan2(-1, 1)), -45)
        self.assertAlmostEqual(math.degrees(math.atan2(1, 0)), 90)

    def test_worked_quadrant_explanation_in_all_locales(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        for locale in locales:
            with self.subTest(locale=locale):
                body = (ROOT / "docs" / locale / "TRIGONOMETRY.md").read_text(
                    encoding="utf-8")
                for token in (r"\arctan\left(\frac{y}{x}\right)",
                              r"\operatorname{atan2}(+1, -1)=+135^\circ",
                              r"\arctan(-1)=-45^\circ",
                              "notes/04-coordinate-frames.md",
                              "two_link_cosine_law.svg"):
                    self.assertIn(token, body)
                self.assertEqual(body.count(
                    r"\operatorname{atan2}(+1, -1)"), 1)


if __name__ == "__main__":
    unittest.main()
