"""Numerical frame-inverse checks and localized tf2 teaching parity.

The lesson describes abstract coordinates only. No ROS nodes or devices run.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def matvec(m, vec):
    return tuple(sum(row[k] * vec[k] for k in range(len(vec))) for row in m)


def transpose(m):
    return tuple(tuple(m[j][i] for j in range(len(m))) for i in range(len(m)))


class Tf2InverseFrameMath(unittest.TestCase):
    def test_identity_rotation_reverses_translation(self):
        identity = ((1.0, 0.0), (0.0, 1.0))
        offset = (0.1, 0.0)
        inverted = matvec(transpose(identity), tuple(-v for v in offset))
        self.assertAlmostEqual(inverted[0], -0.1)
        self.assertAlmostEqual(inverted[1], 0.0)

    def test_rotated_inverse_uses_transpose_not_negated_offset(self):
        rotation = ((0.0, -1.0), (1.0, 0.0))
        translation = (0.1, 0.0)
        inverse_rotation = transpose(rotation)
        inverse_translation = matvec(inverse_rotation,
                                     tuple(-v for v in translation))
        self.assertAlmostEqual(inverse_translation[0], 0.0)
        self.assertAlmostEqual(inverse_translation[1], 0.1)
        self.assertNotEqual(inverse_translation, (-0.1, 0.0))

        child_point = (0.0, 0.05)
        rotated = matvec(rotation, child_point)
        parent_point = tuple(rotated[i] + translation[i] for i in range(2))
        self.assertAlmostEqual(parent_point[0], 0.05)
        self.assertAlmostEqual(parent_point[1], 0.0)
        inverted = matvec(inverse_rotation,
                          tuple(parent_point[i] - translation[i]
                                for i in range(2)))
        for actual, expected in zip(inverted, child_point):
            self.assertAlmostEqual(actual, expected)

    def test_all_locales_contain_both_cases_and_consistent_units(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        self.assertTrue(locales)
        for locale in locales:
            with self.subTest(locale=locale):
                body = (ROOT / "docs" / locale / "notes" /
                        "06-ros2-foundations.md").read_text(encoding="utf-8")
                start, end = '<a id="section-7"></a>', '<a id="section-8"></a>'
                self.assertEqual(body.count(start), 1)
                self.assertEqual(body.count(end), 1)
                section = body.split(start, 1)[1].split(end, 1)[0]
                for token in ("base_link", "tool", "0.1", "0.05",
                              r"{}^{B}\mathbf p_{T}=(0.1, 0, 0)",
                              r"\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}",
                              r"\begin{bmatrix}0\\0.1\end{bmatrix}",
                              r"\begin{bmatrix}0.05\\0\end{bmatrix}",
                              r"\mathrm{m}", "04-coordinate-frames.md#section-3"):
                    self.assertIn(token, section)
                self.assertEqual(sum(line.strip() == "$$"
                                     for line in section.splitlines()), 8)
                self.assertNotIn("\n$\n", section)


if __name__ == "__main__":
    unittest.main()
