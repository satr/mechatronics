"""Guard conceptual ROS 2 tf2/URDF data flow in all language editions.

This checks shared technical terms, not linguistic quality or live ROS behavior.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))
CHAPTER = "notes/06-ros2-foundations.md"


def section(text: str, number: int) -> str:
    start = f'<a id="section-{number}"></a>'
    finish = f'<a id="section-{number+1}"></a>'
    if text.count(start) != 1 or text.count(finish) != 1:
        raise AssertionError(f"Missing or repeated section {number}")
    return text.split(start, 1)[1].split(finish, 1)[0]


class Ros2FrameAndUrdfTranslationParity(unittest.TestCase):
    def test_timestamped_frame_query_has_a_complete_chain(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                text = (ROOT / "docs" / locale / CHAPTER).read_text(
                    encoding="utf-8"
                )
                frames = section(text, 7)
                for required in (
                    "map → odom → base_link → camera_link",
                    "camera_link", "map", "odom", "base_link",
                    "tf2", "static", "dynamic", "lookup", "extrapolation",
                ):
                    self.assertIn(required.lower(), frames.lower())

    def test_robot_model_requires_joint_states_for_moving_transforms(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                text = (ROOT / "docs" / locale / CHAPTER).read_text(
                    encoding="utf-8"
                )
                urdf = section(text, 8)
                for required in (
                    "URDF", "robot_state_publisher",
                    "fixed", "static", "dynamic",
                    "/joint_states", "sensor_msgs/msg/JointState",
                ):
                    self.assertIn(required, urdf)



if __name__ == "__main__":
    unittest.main()
