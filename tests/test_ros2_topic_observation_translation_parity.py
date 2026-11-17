"""Guard the ROS 2 topic discovery-versus-delivery explanation in all locales.

This is a structural teaching regression test, not a DDS runtime test.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "notes/06-ros2-foundations.md"


class Ros2TopicObservationParity(unittest.TestCase):
    def test_synthetic_late_subscriber_trace_has_diagnostic_sequence(self):
        locales = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())
        self.assertTrue(locales)
        for locale in locales:
            with self.subTest(locale=locale):
                text = (ROOT / "docs" / locale / LESSON).read_text(encoding="utf-8")
                start, end = '<a id="section-2"></a>', '<a id="section-3"></a>'
                self.assertEqual(text.count(start), 1)
                self.assertEqual(text.count(end), 1)
                topic = text.split(start, 1)[1].split(end, 1)[0].lower()
                for phrase in ("sample 1", "/sample_source", "/sample_monitor",
                               "volatile", "received 0 samples", "ros2 topic list -t",
                               "ros2 topic info /training/status -v", "qos",
                               "ros_domain_id"):
                    self.assertIn(phrase, topic)


if __name__ == "__main__":
    unittest.main()
