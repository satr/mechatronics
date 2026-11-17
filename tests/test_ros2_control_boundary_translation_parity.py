"""Structural regression: controller manager is not the synthetic topic/service lab.

This is not a linguistic review or a live ROS 2 control-system test.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "notes/06-ros2-foundations.md"
SOURCE = "https://control.ros.org/jazzy/doc/getting_started/getting_started.html"


class Ros2ControlBoundaryParity(unittest.TestCase):
    def test_controller_resource_and_demo_boundary(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        self.assertTrue(locales)
        for locale in locales:
            with self.subTest(locale=locale):
                text = (ROOT / "docs" / locale / LESSON).read_text(encoding="utf-8")
                start, finish = '<a id="section-9"></a>', '<a id="section-10"></a>'
                self.assertEqual(text.count(start), 1)
                self.assertEqual(text.count(finish), 1)
                body = text.split(start, 1)[1].split(finish, 1)[0]
                for term in ("controller_manager", "state interfaces", "command interfaces",
                             "joint1/position", "/training/status", "/training/count", SOURCE):
                    self.assertIn(term.lower(), body.lower())


if __name__ == "__main__":
    unittest.main()
