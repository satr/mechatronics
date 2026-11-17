"""Guard the distinction between ROS 2 image build, startup and graph readiness.

No Docker or ROS commands are executed by these offline source checks.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir()))
LESSON = "notes/06-ros2-foundations.md"
FENCE = chr(96) * 3
BUILD = (
    FENCE + "bash\n"
    "source /opt/ros/${ROS_DISTRO}/setup.bash\n"
    "colcon build --packages-select telemetry_demo\n"
    + FENCE
)
STARTUP = (
    FENCE + "bash\n"
    "source /opt/ros/${ROS_DISTRO}/setup.bash\n"
    "source /opt/training_ws/install/setup.bash\n"
    "exec ros2 launch telemetry_demo demo.launch.py\n"
    + FENCE
)
OLD_COMBINED = (
    "source /opt/ros/${ROS_DISTRO}/setup.bash\n"
    "colcon build --packages-select telemetry_demo\n"
    "source /opt/training_ws/install/setup.bash"
)

def section(doc: str, number: int) -> str:
    a = f'<a id="section-{number}"></a>'
    b = f'<a id="section-{number+1}"></a>'
    if doc.count(a) != 1 or doc.count(b) != 1:
        raise AssertionError(f"Missing or repeated section {number}")
    return doc.split(a, 1)[1].split(b, 1)[0]

class Ros2BuildAndReadinessParity(unittest.TestCase):
    def test_dockerfile_has_distinct_build_and_runtime_commands(self):
        source = (ROOT / "ros2" / "Dockerfile").read_text(encoding="utf-8")
        self.assertIn("RUN source /opt/ros/${ROS_DISTRO}/setup.bash && colcon build", source)
        self.assertIn(
            'CMD ["/bin/bash", "-lc", "source /opt/ros/${ROS_DISTRO}/setup.bash '
            '&& source /opt/training_ws/install/setup.bash '
            '&& exec ros2 launch telemetry_demo demo.launch.py"]', source
        )

    def test_each_locale_distinguishes_build_and_startup(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                lesson = (ROOT / "docs" / locale / LESSON).read_text(
                    encoding="utf-8"
                )
                packages = section(lesson, 4)
                self.assertEqual(packages.count(BUILD), 1)
                self.assertEqual(packages.count(STARTUP), 1)
                self.assertNotIn(OLD_COMBINED, packages)
                self.assertLess(
                    packages.index(chr(96) + "RUN" + chr(96)),
                    packages.index(chr(96) + "CMD" + chr(96)),
                )
                for name in ("package.xml", "setup.py", "build/", "install/"):
                    self.assertIn(name, packages)

    def test_launch_does_not_imply_receiving_a_sample(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                lesson = (ROOT / "docs" / locale / LESSON).read_text(
                    encoding="utf-8"
                )
                launch = section(lesson, 6)
                for concept in (
                    "launch_ros.actions.Node", "interval_s=1.0",
                    "/training/status", "/training/count",
                    "received 0 samples",
                ):
                    self.assertIn(concept, launch)

if __name__ == "__main__":
    unittest.main()
