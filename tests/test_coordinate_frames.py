"""Independent numerical checks for the documented planar geometry examples."""
from __future__ import annotations

import math
import unittest


def local_to_world(x: float, y: float, ox: float, oy: float, degrees: float) -> tuple[float, float]:
    angle = math.radians(degrees)
    return (ox + x * math.cos(angle) - y * math.sin(angle),
            oy + x * math.sin(angle) + y * math.cos(angle))


def forward_two_link(l1: float, l2: float, first_degrees: float, relative_degrees: float) -> tuple[float, float]:
    a1 = math.radians(first_degrees)
    a2 = math.radians(first_degrees + relative_degrees)
    return (l1 * math.cos(a1) + l2 * math.cos(a2),
            l1 * math.sin(a1) + l2 * math.sin(a2))


class CoordinateFrameExamples(unittest.TestCase):
    def assert_point(self, observed: tuple[float, float], expected: tuple[float, float]) -> None:
        self.assertAlmostEqual(observed[0], expected[0], places=8)
        self.assertAlmostEqual(observed[1], expected[1], places=8)

    def test_local_world_transforms(self) -> None:
        self.assert_point(local_to_world(0, 10, 100, 50, 90), (90, 50))
        self.assert_point(local_to_world(20, 0, 100, 50, 90), (100, 70))

    def test_sensor_frame_chain(self) -> None:
        origin = local_to_world(20, 0, 100, 50, 90)
        self.assert_point(local_to_world(0, 10, origin[0], origin[1], 90), (90, 70))

    def test_two_link_forward_kinematics(self) -> None:
        self.assert_point(forward_two_link(100, 50, 30, 60), (50 * math.sqrt(3), 100))

    def test_both_elbow_branches(self) -> None:
        self.assert_point(forward_two_link(100, 100, 0, 90), (100, 100))
        self.assert_point(forward_two_link(100, 100, 90, -90), (100, 100))

    def test_reachable_annulus(self) -> None:
        inner, outer = abs(100 - 50), 100 + 50
        self.assertEqual((inner, outer), (50, 150))
        self.assertTrue(inner <= math.hypot(0, 120) <= outer)
        self.assertFalse(inner <= math.hypot(0, 0) <= outer)

    def test_cosine_rule(self) -> None:
        cosine = (120**2 - 100**2 - 50**2) / (2 * 100 * 50)
        self.assertAlmostEqual(cosine, 0.19, places=8)
        self.assertAlmostEqual(math.degrees(math.acos(cosine)), 79.0472, places=3)


if __name__ == "__main__":
    unittest.main()
