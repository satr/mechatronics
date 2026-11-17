"""Guard the average-velocity versus path-speed distinction across translations."""
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))


class MotionSpeedTranslationParity(unittest.TestCase):
    def test_every_locale_keeps_both_worked_averages(self):
        speed_formula = (
            r"\overline{\lvert v\rvert}"
            r"=\frac{12\ \mathrm{mm}}{4\ \mathrm{s}}=3\ \mathrm{mm/s}"
        )
        velocity_formula = (
            r"\overline{v}_x"
            r"=\frac{0\ \mathrm{mm}}{4\ \mathrm{s}}=0\ \mathrm{mm/s}"
        )
        for locale in LOCALES:
            with self.subTest(locale=locale):
                body = (ROOT / "docs" / locale / "notes" /
                        "01-motion-calculus.md").read_text(encoding="utf-8")
                first = body.split('<a id="section-1"></a>', 1)[1].split(
                    '<a id="section-2"></a>', 1
                )[0]
                self.assertEqual(first.count(velocity_formula), 1)
                self.assertEqual(first.count(speed_formula), 1)
                self.assertIn("12", first)

    def test_integral_example_is_not_confused_with_derivative_model(self):
        # Two teaching sections deliberately use different synthetic
        # functions: d(2*t^2)/dt = 4*t, while int(2*t)dt = t^2 + C.
        # Omitting this distinction in translated prose suggests that
        # the integrand should be the previous section's derivative.
        for locale in LOCALES:
            with self.subTest(locale=locale):
                lesson = (ROOT / "docs" / locale / "notes" /
                          "01-motion-calculus.md").read_text(encoding="utf-8")
                section = lesson.split('<a id="section-3"></a>', 1)[1].split(
                    '<a id="section-4"></a>', 1)[0]
                for expression in (
                    "x(t)=2t^2", "v(t)=4t", "v(t)=2t", "x(t)=t^2+C",
                ):
                    self.assertIn(expression, section)
                self.assertIn("4\\ \\mathrm{mm}", section)

    def test_independent_piecewise_constant_motion(self):
        segments = [(3.0, 2.0), (-3.0, 2.0)]  # mm/s and s
        elapsed = sum(duration for _, duration in segments)
        displacement = sum(v * duration for v, duration in segments)
        traveled = sum(abs(v) * duration for v, duration in segments)
        self.assertTrue(math.isclose(elapsed, 4))
        self.assertTrue(math.isclose(displacement / elapsed, 0))
        self.assertTrue(math.isclose(traveled / elapsed, 3))
        self.assertNotEqual(traveled, abs(displacement))


if __name__ == "__main__":
    unittest.main()
