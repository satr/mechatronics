"""Check conceptual and algebraic parity of the planar velocity lesson.

Shared equations can be checked mechanically; prose must still receive native
semantic review. The checks guard against deleting intermediate reasoning.
"""
from __future__ import annotations

import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))
LESSON = "notes/05-velocity-jacobian.md"


def section(text: str, number: int) -> str:
    start = f'<a id="section-{number}"></a>'
    end = f'<a id="section-{number+1}"></a>'
    if text.count(start) != 1:
        raise AssertionError(f"Expected exactly one {start}")
    if number < 7 and text.count(end) != 1:
        raise AssertionError(f"Expected exactly one {end}")
    return text.split(start, 1)[1].split(end, 1)[0]


class VelocityTranslationParity(unittest.TestCase):
    def test_arc_to_instantaneous_speed_chain_in_all_editions(self):
        required = (
            r"\Delta s=L\lvert\Delta Q\rvert",  # exact nonnegative arc length
            r"\Delta s_{\mathrm{signed}}=L\Delta Q",  # signed arc coordinate
            r"\overline{v}=\frac{\Delta s}{\Delta t}",  # average speed
            r"\frac{\Delta Q}{\Delta t}",  # angular increment / elapsed time
            r"\Delta t\to0",  # instantaneous limit, not an unexplained jump
            r"\omega=\dot Q=\mathrm{d}Q/\mathrm{d}t",  # angular rate
            r"v=L\lvert\dot Q\rvert",  # final speed magnitude
        )
        for locale in LOCALES:
            with self.subTest(locale=locale):
                body = (ROOT / "docs" / locale / LESSON).read_text(encoding="utf-8")
                first = section(body, 1)
                for expression in required:
                    self.assertIn(expression, first)
                # Incorrect replacement of the exact arc length by a small-angle
                # approximation was the original regression.
                self.assertNotIn("Δs≈LΔQ", first)
                self.assertEqual(first.count("link_tangent_velocity.svg"), 1)

    def test_zero_radius_exception_is_not_lost_in_translation(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                body = (ROOT / "docs" / locale / LESSON).read_text(encoding="utf-8")
                fifth = section(body, 5)
                for expression in (
                    r"\frac{\mathrm{d}r}{\mathrm{d}Q_2}",
                    r"$r>0$", r"$L_1=L_2$", r"$r=0$",
                ):
                    self.assertIn(expression, fifth)

    def test_common_model_and_solved_examples_remain_available(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                body = (ROOT / "docs" / locale / LESSON).read_text(encoding="utf-8")
                for number in range(1, 8):
                    self.assertTrue(section(body, number).strip())
                self.assertIn(r"\omega_1=\dot{Q}_1", section(body, 2))
                self.assertIn(r"\Delta x_{\mathrm{axis}}", section(body, 6))
                self.assertIn(r"\Delta r", section(body, 6))
                self.assertIn(r"\det J=L_1L_2\sin(Q_2)", section(body, 7))
                checks = section(body, 7)
                for n in range(1, 5):
                    self.assertRegex(checks, rf"(?m)^{n}\. ")
                for number in ("10.61", "8.66", "0.010", "0.020"):
                    self.assertIn(number, checks)

    def test_previous_condensed_worked_answers_have_intermediate_steps(self):
        for locale in set(LOCALES) - {"en", "ru", "ko", "fi"}:
            with self.subTest(locale=locale):
                body = (ROOT / "docs" / locale / LESSON).read_text(encoding="utf-8")
                checks = section(body, 7)
                self.assertIn("-5-15=-20", checks)
                self.assertIn(r"25\delta^2=25\cdot0.02^2=0.010", checks)
                self.assertIn(r"50\delta=1.000", checks)

    def test_jacobian_determinant_chain_in_all_editions(self):
        expressions = (
            r"J_{11}=\frac{\partial X}{\partial Q_1}",
            r"J_{12}=\frac{\partial X}{\partial Q_2}",
            r"J_{21}=\frac{\partial Y}{\partial Q_1}",
            r"J_{22}=\frac{\partial Y}{\partial Q_2}",
            r"\det J=J_{11}J_{22}-J_{12}J_{21}",
            r"\det J=L_1L_2\bigl[\sin(Q_1+Q_2)\cos(Q_1)",
            r"\det J=L_1L_2\sin\bigl((Q_1+Q_2)-Q_1\bigr)",
            r"\det J=L_1L_2\sin(Q_2)",
        )
        for locale in LOCALES:
            with self.subTest(locale=locale):
                body = (ROOT / "docs" / locale / LESSON).read_text(encoding="utf-8")
                seventh = section(body, 7)
                for expression in expressions:
                    self.assertIn(expression, seventh)
                self.assertEqual(seventh.count("two_link_jacobian_velocity.svg"), 1)
        # Independent numerical identity and vector-sum check.
        l1, l2 = 100.0, 50.0
        for q1, q2 in ((math.pi / 6, math.pi / 3), (0, 0),
                       (0.7, -1.1), (0.5, math.pi)):
            a = -l1 * math.sin(q1) - l2 * math.sin(q1 + q2)
            b = -l2 * math.sin(q1 + q2)
            c = l1 * math.cos(q1) + l2 * math.cos(q1 + q2)
            d = l2 * math.cos(q1 + q2)
            self.assertAlmostEqual(a * d - b * c,
                                   l1 * l2 * math.sin(q2), places=9)
        q1, q2 = math.pi / 6, math.pi / 3
        vx = (-100 * math.sin(q1) - 50 * math.sin(q1 + q2)) * 0.1 - 50 * math.sin(q1 + q2) * 0.2
        vy = (100 * math.cos(q1) + 50 * math.cos(q1 + q2)) * 0.1 + 50 * math.cos(q1 + q2) * 0.2
        self.assertAlmostEqual(vx, -20.0)
        self.assertAlmostEqual(vy, 5 * math.sqrt(3))

    def test_angular_speed_example_independently_from_tip_positions(self):
        length, theta, omega, dt = 150.0, math.pi / 4, 0.1, 1e-5
        arc_length = length * abs(omega * dt)
        average_speed = arc_length / dt
        self.assertAlmostEqual(average_speed, 15.0)
        before = (length * math.cos(theta - omega * dt),
                  length * math.sin(theta - omega * dt))
        after = (length * math.cos(theta + omega * dt),
                 length * math.sin(theta + omega * dt))
        vx = (after[0] - before[0]) / (2 * dt)
        vy = (after[1] - before[1]) / (2 * dt)
        self.assertLess(vx, 0)
        self.assertGreater(vy, 0)
        self.assertAlmostEqual(math.hypot(vx, vy), average_speed, places=8)


if __name__ == "__main__":
    unittest.main()
