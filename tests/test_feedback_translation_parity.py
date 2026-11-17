"""Check PID teaching examples and translations against independently computed values."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))
PATH = "notes/03-feedback-control.md"


def section(text: str, number: int) -> str:
    start = f'<a id="section-{number}"></a>'
    end = f'<a id="section-{number+1}"></a>'
    if text.count(start) != 1 or text.count(end) != 1:
        raise AssertionError(f"Missing or duplicate section anchor {number}")
    return text.split(start, 1)[1].split(end, 1)[0]


def pi_rows(markdown: str) -> list[tuple[float, ...]]:
    """Parse the six numeric rows of the documented worked example."""
    lines = markdown.splitlines()
    header = next(i for i, line in enumerate(lines) if line.startswith("| k |"))
    if "I_set (A)" not in lines[header] or "u_P (A)" not in lines[header]:
        raise AssertionError("Missing P/I/total current columns")
    values = []
    for line in lines[header+2:]:
        if not line.startswith("| "):
            break
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 7:
            raise AssertionError("Expected 7 table columns")
        values.append(tuple(float(cell.replace("−", "-")) for cell in cells))
    return values


class PIDWorkedExampleParity(unittest.TestCase):
    def test_localized_warning_and_complete_current_command(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                lesson = (ROOT / "docs" / locale / PATH).read_text(encoding="utf-8")
                warning = next(line for line in lesson.splitlines() if line.startswith("> "))
                self.assertIn("**", warning)
                if locale != "en":
                    self.assertNotIn(
                        "These simplified algorithms must not be connected",
                        warning,
                    )
                portion = section(lesson, 3)
                for identifier in (
                    "integral += error * 1.0",
                    "p_command = 0.02 * error",
                    "i_command = 0.002 * integral",
                    "current_setpoint = p_command + i_command",
                ):
                    self.assertIn(identifier, portion)

                rows = pi_rows(portion)
                self.assertEqual(len(rows), 6)
                accumulated = 0.0
                speeds = [950, 950, 950, 1000, 1020, 1020]
                for k, speed in enumerate(speeds, 1):
                    error = 1000.0 - speed
                    accumulated += error * 1.0
                    proportional = 0.02 * error
                    integral = 0.002 * accumulated
                    current_setpoint = proportional + integral
                    expected = (k, speed, error, accumulated,
                                proportional, integral, current_setpoint)
                    for observed, calculated in zip(rows[k-1], expected):
                        self.assertAlmostEqual(observed, calculated, places=10)

    def test_all_editions_derive_the_derivative_gain_units(self):
        # The D term differentiates an error expressed in rpm; its output
        # is a current setpoint in A. Omitting K_d units breaks the
        # dimensional reasoning, even when the numeric example survives.
        formula = r"[K_d]=\mathrm{A\cdot s/rpm}"
        derivative = r"u_D=K_d\frac{\mathrm{d}\varepsilon}{\mathrm{d}t}"
        for locale in LOCALES:
            with self.subTest(locale=locale):
                lesson = (ROOT / "docs" / locale / PATH).read_text(
                    encoding="utf-8")
                body = section(lesson, 4)
                self.assertIn(derivative, body)
                self.assertEqual(body.count(formula), 1)
                self.assertIn("800\\ \\mathrm{rpm/s}", body)
                # Require an explicit reasoning sentence, not only a
                # copied equation, while keeping language-specific prose.
                self.assertIn("A·s/rpm", body)
                self.assertIn("rpm/s", body)
                self.assertIn("`K_d`", body)

    def test_pi_command_is_not_the_change_in_integrator(self):
        accumulated = 150.0
        previous_integral = 0.002 * accumulated
        accumulated += -20.0
        next_integral = 0.002 * accumulated
        proportional = 0.02 * -20.0
        self.assertAlmostEqual(next_integral - previous_integral, -0.04)
        self.assertAlmostEqual(proportional + next_integral, -0.14)
        self.assertNotAlmostEqual(proportional + next_integral,
                                  next_integral - previous_integral)


if __name__ == "__main__":
    unittest.main()
