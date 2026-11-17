"""Guard minimum explanatory ROS 2 glossary coverage across all editions.

Structure and common technical identifiers only; human semantic review remains necessary.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "notes/06-ros2-foundations.md"


class Ros2GlossaryParity(unittest.TestCase):
    def test_distinct_entries_and_boundaries(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        self.assertTrue(locales)
        for locale in locales:
            with self.subTest(locale=locale):
                text = (ROOT / "docs" / locale / LESSON).read_text(encoding="utf-8")
                anchor = '<a id="section-12"></a>'
                self.assertEqual(text.count(anchor), 1)
                tail = text.split(anchor, 1)[1]
                self.assertIn("\n\n**", tail)
                entries = tail.split("\n\n**", 1)[0]
                bullets = [line for line in entries.splitlines() if line.startswith("- **")]
                self.assertEqual(len(bullets), 15)
                lower = entries.lower()
                for term in ("node", "ros graph", "topic", "message",
                             "publisher", "subscriber", "service", "action",
                             "parameter", "rmw", "dds", "colcon", "ament",
                             "launch", "tf2", "urdf", "robot_state_publisher",
                             "ros2_control", "qos"):
                    self.assertIn(term, lower)


if __name__ == "__main__":
    unittest.main()
