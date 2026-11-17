"""Static checks for the plain official-image ROS Docker walkthrough.

Bash blocks are syntax-checked; real Docker is exercised only on trusted main.
"""
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROS = ROOT / "ros2"
LOCALES = tuple(sorted(x.name for x in (ROOT / "docs").iterdir() if x.is_dir()))


class PlainDockerGuide(unittest.TestCase):
    def test_commands_are_copyable_bash(self):
        guide = (ROS / "PLAIN_DOCKER.md").read_text(encoding="utf-8")
        blocks = re.findall(r"```bash\n(.*?)\n```", guide, re.S)
        self.assertEqual(len(blocks), 11)
        for i, block in enumerate(blocks):
            with self.subTest(block=i):
                subprocess.run(["bash", "-n"], input=block, text=True,
                               check=True, capture_output=True)
        self.assertIn("docker run -d --name ros -e ROS_DOMAIN_ID=42 ros:jazzy-ros-base sleep infinity", guide)
        self.assertIn("docker exec -it ros bash", guide)
        self.assertIn("docker exec -it ros bash -ic 'ros2 run demo_nodes_cpp talker'", guide)
        self.assertIn("docker exec -it ros bash -ic 'ros2 run demo_nodes_py listener'", guide)
        self.assertIn("docker stop ros", guide)
        self.assertIn("docker start ros", guide)
        self.assertIn("docker cp ros2/control_lab/. ros:/opt/control_lab", guide)
        self.assertIn("colcon build --packages-select telemetry_demo", guide)
        self.assertNotIn("export ROS_DISTRO=jazzy", guide)
        self.assertNotIn("-e ROS_DISTRO", guide.split("## 2.", 1)[0].split("```bash")[1])
        self.assertIn('source "/opt/ros/${ROS_DISTRO}/setup.bash"', guide)
        self.assertIn("LD_LIBRARY_PATH", guide)
        self.assertIn("conditional workaround", guide)

    def test_prepared_images_inherit_distro_and_auto_source(self):
        for path in (ROS / "Dockerfile", ROS / "control_lab" / "Dockerfile"):
            with self.subTest(path=path.name):
                code = path.read_text(encoding="utf-8")
                self.assertIn("FROM ros:jazzy-ros-base", code)
                self.assertNotIn("ENV ROS_DISTRO=", code)
                self.assertNotIn("ros-jazzy-", code)
                self.assertNotIn("/opt/ros/jazzy", code)
                self.assertIn("ros-${ROS_DISTRO}-", code)
                self.assertIn("/root/.bashrc", code)
                self.assertIn("CMD", code)
        for path in (ROS / "smoke_test.sh", ROS / "control_lab" / "smoke_test.sh",
                     ROS / "plain_docker_smoke.sh"):
            with self.subTest(path=str(path)):
                subprocess.run(["bash", "-n", str(path)], check=True,
                               capture_output=True)
                code = path.read_text(encoding="utf-8")
                self.assertNotIn("/opt/ros/jazzy", code)
        ci = (ROOT / ".github" / "workflows" / "ros2-live-smoke.yml").read_text(encoding="utf-8")
        self.assertIn("bash ros2/plain_docker_smoke.sh", ci)
        self.assertIn("branches: [main]", ci)
        self.assertNotIn("pull_request:", ci)

    def test_all_locales_link_single_shared_setup(self):
        for l in LOCALES:
            with self.subTest(locale=l):
                for file in ("README.md", "notes/06-ros2-foundations.md",
                             "notes/07-ros2-control-lab.md"):
                    txt = (ROOT / "docs" / l / file).read_text(encoding="utf-8")
                    self.assertIn("PLAIN_DOCKER.md", txt)
                for file in ("notes/06-ros2-foundations.md",
                             "notes/07-ros2-control-lab.md"):
                    txt = (ROOT / "docs" / l / file).read_text(encoding="utf-8")
                    self.assertNotIn("ROS_DISTRO=jazzy", txt)
                    self.assertNotIn("/opt/ros/jazzy", txt)
                    self.assertNotIn("ros-jazzy-ros2-control", txt)


if __name__ == "__main__":
    unittest.main()
