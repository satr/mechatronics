"""Verify the complete W->T->S matrix composition example in every locale."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


class FrameChainWorkedMatrixParity(unittest.TestCase):
    def test_independent_matrix_product_and_sensor_point(self):
        wt = ((0, -1, 100), (1, 0, 50), (0, 0, 1))
        ts = ((1, 0, 20), (0, 1, 0), (0, 0, 1))
        ws = matmul(wt, ts)
        self.assertEqual(ws, ((0, -1, 100), (1, 0, 70), (0, 0, 1)))
        p = (0, 10, 1)
        self.assertEqual(tuple(sum(ws[i][j] * p[j] for j in range(3))
                               for i in range(3)), (90, 70, 1))
        self.assertNotEqual(matmul(ts, wt), ws)

    def test_all_localized_chapters_retain_composition_steps(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        self.assertTrue(locales)
        for locale in locales:
            with self.subTest(locale=locale):
                source = (ROOT / "docs" / locale / "notes" /
                          "04-coordinate-frames.md").read_text(encoding="utf-8")
                a, b = '<a id="section-3"></a>', '<a id="section-4"></a>'
                self.assertEqual(source.count(a), 1)
                self.assertEqual(source.count(b), 1)
                part = source.split(a, 1)[1].split(b, 1)[0]
                required = (r"T_{WT}=", r"T_{TS}=", r"T_{WS}=T_{WT}T_{TS}=",
                            r"0 & -1 & 100\\", r"1 & 0 & 70\\",
                            r"\begin{bmatrix}0\\10\\1\end{bmatrix}",
                            r"\begin{bmatrix}90\\70\\1\end{bmatrix}",
                            "06-ros2-foundations.md#section-7")
                for token in required:
                    self.assertIn(token, part)
                self.assertEqual(sum(line.strip() == "$$"
                                     for line in part.splitlines()), 8)


if __name__ == "__main__":
    unittest.main()
