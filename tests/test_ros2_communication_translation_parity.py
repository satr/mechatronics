"""Structural concept parity for ROS 2 communication choices and DDS diagnosis.

Exact technical tokens can be checked without executing ROS; localized meaning
must still receive human review. This is not a network or QoS integration test.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))
DOC = "notes/06-ros2-foundations.md"
QOS_DOCS = "https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html"


def section(text: str, number: int) -> str:
    current = f'<a id="section-{number}"></a>'
    following = f'<a id="section-{number+1}"></a>'
    if text.count(current) != 1 or text.count(following) != 1:
        raise AssertionError(f"Missing/duplicate section {number}")
    return text.split(current, 1)[1].split(following, 1)[0]


class Ros2CommunicationTranslationParity(unittest.TestCase):
    def test_mechanism_selection_has_four_clear_pitfalls(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                doc = (ROOT / "docs" / locale / DOC).read_text(encoding="utf-8")
                guidance = section(doc, 3)
                for mechanism in ("Topic", "Service", "Action", "Parameter"):
                    rows = [
                        line for line in guidance.splitlines()
                        if line.startswith(f"| {mechanism} |")
                    ]
                    self.assertEqual(len(rows), 1, mechanism)
                    self.assertEqual(len(rows[0].strip("|").split("|")), 4)
                for term in ("/training/count", "interval_s=1.0"):
                    self.assertIn(term, guidance)

    def test_diagnostic_order_and_qos_mismatch_not_lost(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                text = (ROOT / "docs" / locale / DOC).read_text(encoding="utf-8")
                qos = section(text, 10)
                for term in (
                    "best_effort", "reliable", "volatile", "transient_local",
                    "ROS_DOMAIN_ID=42", "ros2 node list",
                    "ros2 topic info /training/status -v",
                    "docker compose logs demo",
                ):
                    self.assertIn(term, qos)
                self.assertIn(QOS_DOCS, text)

    def test_reliability_request_offered_example_is_directional(self):
        # Simplified reliability-only check, not the full DDS compatibility matrix.
        level = {"best_effort": 0, "reliable": 1}
        compatible = lambda requested, offered: (
            level[requested] <= level[offered]
        )
        self.assertFalse(compatible("reliable", "best_effort"))
        self.assertTrue(compatible("best_effort", "reliable"))
        self.assertTrue(compatible("reliable", "reliable"))


if __name__ == "__main__":
    unittest.main()
