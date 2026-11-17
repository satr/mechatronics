"""Numerical tests of synthetic 2D kinematics, derivatives and SVG reference diagrams."""
import math
import pathlib
import unittest
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]


def tip(length, angle):
    return length * math.cos(angle), length * math.sin(angle)


def velocity(length, angle, omega):
    return -length * math.sin(angle) * omega, length * math.cos(angle) * omega


def radius(l1, l2, elbow):
    return math.sqrt(l1 * l1 + l2 * l2 + 2 * l1 * l2 * math.cos(elbow))


class KinematicsAndFigureTests(unittest.TestCase):
    def test_reference_angles_and_signs(self):
        known = (
            (0, 1.0, 0.0), (30, math.sqrt(3)/2, 0.5),
            (45, math.sqrt(2)/2, math.sqrt(2)/2),
            (60, 0.5, math.sqrt(3)/2), (90, 0.0, 1.0),
            (120, -0.5, math.sqrt(3)/2),
            (135, -math.sqrt(2)/2, math.sqrt(2)/2),
            (150, -math.sqrt(3)/2, 0.5), (180, -1, 0),
            (210, -math.sqrt(3)/2, -0.5),
            (225, -math.sqrt(2)/2, -math.sqrt(2)/2),
            (240, -0.5, -math.sqrt(3)/2), (270, 0, -1),
            (300, 0.5, -math.sqrt(3)/2),
            (315, math.sqrt(2)/2, -math.sqrt(2)/2),
            (330, math.sqrt(3)/2, -0.5),
        )
        for a, c, s in known:
            self.assertAlmostEqual(math.cos(math.radians(a)), c)
            self.assertAlmostEqual(math.sin(math.radians(a)), s)

    def test_single_link_chain_rule_finite_difference(self):
        L, Q, omega, dt = 150, math.pi / 4, 0.1, 1e-5
        x0, y0 = tip(L, Q)
        x1, y1 = tip(L, Q + omega * dt)
        vx, vy = velocity(L, Q, omega)
        self.assertAlmostEqual((x1-x0)/dt, vx, places=4)
        self.assertAlmostEqual((y1-y0)/dt, vy, places=4)
        self.assertAlmostEqual(math.hypot(vx, vy), L * omega)
        self.assertAlmostEqual(velocity(L, Q, -omega)[0], -vx)

    def test_two_joint_velocity(self):
        q1, q2 = math.radians(30), math.radians(60)
        dq1, dq2 = .1, .2
        vx = -100 * math.sin(q1) * dq1 - 50 * math.sin(q1+q2) * (dq1+dq2)
        vy = 100 * math.cos(q1) * dq1 + 50 * math.cos(q1+q2) * (dq1+dq2)
        self.assertAlmostEqual(vx, -20)
        self.assertAlmostEqual(vy, 5*math.sqrt(3), places=7)


    def test_two_joint_jacobian_against_independent_position_differences(self):
        """Check both Jacobian columns against central differences of 2R position.

        The position expressions and derivative expressions are evaluated
        independently, including negative elbows and singular postures.
        """
        l1, l2 = 100.0, 80.0  # mm
        step = 1e-5  # rad

        def position(q1, q2):
            return (l1 * math.cos(q1) + l2 * math.cos(q1 + q2),
                    l1 * math.sin(q1) + l2 * math.sin(q1 + q2))

        poses = ((0.0, 0.0),
                 (math.pi / 2, math.pi),
                 (math.radians(30), math.radians(60)),
                 (math.radians(-40), math.radians(-75)))
        for q1, q2 in poses:
            with self.subTest(q1=q1, q2=q2):
                # Analytic columns: the effect of each joint's angular rate.
                j11 = -l1 * math.sin(q1) - l2 * math.sin(q1 + q2)
                j12 = -l2 * math.sin(q1 + q2)
                j21 = l1 * math.cos(q1) + l2 * math.cos(q1 + q2)
                j22 = l2 * math.cos(q1 + q2)

                x_plus, y_plus = position(q1 + step, q2)
                x_minus, y_minus = position(q1 - step, q2)
                dx_dq1 = (x_plus - x_minus) / (2 * step)
                dy_dq1 = (y_plus - y_minus) / (2 * step)
                self.assertAlmostEqual(j11, dx_dq1, delta=1e-6)
                self.assertAlmostEqual(j21, dy_dq1, delta=1e-6)

                x_plus, y_plus = position(q1, q2 + step)
                x_minus, y_minus = position(q1, q2 - step)
                dx_dq2 = (x_plus - x_minus) / (2 * step)
                dy_dq2 = (y_plus - y_minus) / (2 * step)
                self.assertAlmostEqual(j12, dx_dq2, delta=1e-6)
                self.assertAlmostEqual(j22, dy_dq2, delta=1e-6)

                # The determinant depends on relative elbow angle, not q1.
                determinant = j11 * j22 - j12 * j21
                self.assertAlmostEqual(determinant, l1 * l2 * math.sin(q2),
                                       delta=1e-9)

    def test_two_joint_velocity_against_time_step(self):
        """Verify signed Cartesian velocity without differentiating the same formula."""
        l1, l2 = 100.0, 80.0
        q1, q2 = math.radians(35), math.radians(-55)
        w1, w2 = 0.12, -0.25  # rad/s
        dt = 1e-5  # s

        def position(time):
            a1, a2 = q1 + w1 * time, q2 + w2 * time
            return (l1 * math.cos(a1) + l2 * math.cos(a1 + a2),
                    l1 * math.sin(a1) + l2 * math.sin(a1 + a2))

        before = position(-dt)
        after = position(dt)
        measured = tuple((b - a) / (2 * dt) for a, b in zip(before, after))
        expected = (
            -l1 * math.sin(q1) * w1 - l2 * math.sin(q1 + q2) * (w1 + w2),
            l1 * math.cos(q1) * w1 + l2 * math.cos(q1 + q2) * (w1 + w2),
        )
        for actual, analytic in zip(measured, expected):
            self.assertAlmostEqual(actual, analytic, delta=1e-6)

    def test_annulus_and_singularities(self):
        self.assertAlmostEqual(radius(100, 50, 0), 150)
        self.assertAlmostEqual(radius(100, 50, math.pi), 50)
        for q2 in (0, math.pi):
            self.assertAlmostEqual(100 * 50 * math.sin(q2), 0)

    def test_folded_axial_vs_radial_small_angle(self):
        for delta in (0.001, 0.01, 0.02):
            axial = 50 * (1 - math.cos(delta))
            radial = radius(100, 50, math.pi - delta) - 50
            transverse = 50 * math.sin(delta)
            self.assertAlmostEqual(axial / (25 * delta**2), 1, delta=.001)
            self.assertAlmostEqual(radial / (50 * delta**2), 1, delta=.001)
            self.assertAlmostEqual(transverse / (50 * delta), 1, delta=.001)
        self.assertLess(axial, radial)

    def test_six_svg_assets_parse(self):
        files = ("unit_circle_reference.svg", "trig_ratios.svg",
                 "arccos_reference_curve.svg", "link_tangent_velocity.svg",
                 "folded_displacement_curves.svg", "folded_radial_speed.svg")
        for name in files:
            path = ROOT / "assets" / "figures" / name
            tree = ET.parse(path)
            self.assertTrue(tree.getroot().tag.endswith("svg"))
            self.assertNotIn("<script", path.read_text(encoding="utf-8").lower())
        for name in files[:1]:
            content = (ROOT / "assets" / "figures" / name).read_text(encoding="utf-8")
            for angle in (0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330):
                self.assertIn(f"{angle}°", content)
            self.assertIn("√3/2", content)
            self.assertIn("−√3/2", content)
            self.assertIn("cos = 1 ≈ 1.0000", content)



    def test_unit_circle_one_card_per_angle_with_correct_values(self):
        expected = {
            0: ("1", "0"),
            30: ("√3/2", "1/2"),
            45: ("√2/2", "√2/2"),
            60: ("1/2", "√3/2"),
            90: ("0", "1"),
            120: ("−1/2", "√3/2"),
            135: ("−√2/2", "√2/2"),
            150: ("−√3/2", "1/2"),
            180: ("−1", "0"),
            210: ("−√3/2", "−1/2"),
            225: ("−√2/2", "−√2/2"),
            240: ("−1/2", "−√3/2"),
            270: ("0", "−1"),
            300: ("1/2", "−√3/2"),
            315: ("√2/2", "−√2/2"),
            330: ("√3/2", "−1/2"),
        }
        root = ET.parse(ROOT / "assets" / "figures" / "unit_circle_reference.svg").getroot()
        cards = [node for node in root.iter() if node.attrib.get("class") == "angle-card"]
        connectors = [node for node in root.iter() if node.attrib.get("class") == "leader"]
        self.assertEqual(len(cards), 16)
        self.assertEqual(len(connectors), 16)
        self.assertEqual({int(c.get("data-angle")) for c in cards}, set(expected))
        for card in cards:
            angle = int(card.get("data-angle"))
            exact_cos, exact_sin = expected[angle]
            self.assertEqual(card.get("data-cos-exact"), exact_cos)
            self.assertEqual(card.get("data-sin-exact"), exact_sin)
            radians = math.radians(angle)
            self.assertAlmostEqual(float(card.get("data-cos-decimal")), math.cos(radians), places=4)
            self.assertAlmostEqual(float(card.get("data-sin-decimal")), math.sin(radians), places=4)
            texts = [child.text for child in card if child.tag.endswith("text")]
            self.assertEqual(len(texts), 3, angle)
            self.assertEqual(texts[0], f"{angle}°")
            self.assertIn(f"cos = {exact_cos} ≈", texts[1])
            self.assertIn(f"sin = {exact_sin} ≈", texts[2])

    def test_separate_exact_and_decimal_reference_columns(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        for locale in locales:
            content = (ROOT / "docs" / locale / "TRIGONOMETRY.md").read_text(encoding="utf-8")
            lines = content.splitlines()
            start = next(i for i, line in enumerate(lines) if line.startswith("| θ |"))
            rows = []
            for line in lines[start:]:
                if not line.startswith("|"):
                    break
                rows.append([cell.strip() for cell in line.strip("|").split("|")])
            self.assertEqual(len(rows), 18, locale)
            self.assertTrue(all(len(row) == 8 for row in rows), locale)
            self.assertIn("cos θ", rows[0][1])
            self.assertIn("cos θ", rows[0][2])
            self.assertIn("sin θ", rows[0][3])
            self.assertIn("sin θ", rows[0][4])
            self.assertIn("tan θ", rows[0][5])
            self.assertIn("tan θ", rows[0][6])
            self.assertIn("notes/00-calculus-foundations.md", content)
            self.assertIn("notes/03-feedback-control.md", content)
            for row in rows[2:]:
                self.assertRegex(row[2], r"^-?\d+\.\d{4}$")
                self.assertRegex(row[4], r"^-?\d+\.\d{4}$")
                if row[0] not in ("90°", "270°"):
                    self.assertRegex(row[6], r"^-?\d+\.\d{4}$")
                else:
                    self.assertEqual(row[6], "—")

    def test_triangle_svg_intrinsic_dimensions(self):
        svg = ET.parse(ROOT / "assets" / "figures" / "trig_ratios.svg").getroot()
        self.assertEqual(svg.get("width"), "480")
        self.assertEqual(svg.get("height"), "856")
        self.assertEqual(svg.get("viewBox"), "0 0 720 1284")



if __name__ == "__main__":
    unittest.main()
