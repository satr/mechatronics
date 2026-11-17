"""Offline invariants for the independent synthetic Jazzy control lab (not a ROS runtime test)."""
import ast
import math
from pathlib import Path
import re
import subprocess
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "ros2" / "control_lab"
LOCALES = sorted(p.name for p in (ROOT / "docs").iterdir() if p.is_dir())


class JazzyHeadlessControlLab(unittest.TestCase):
    def test_urdf_geometry_and_interfaces(self):
        model = ET.parse(LAB / "arm.urdf").getroot()
        self.assertEqual(model.get("name"), "virtual_arm")
        self.assertEqual({x.get("name") for x in model.findall("link")},
                         {"base_link", "arm_link", "tool"})
        joints = {j.get("name"): j for j in model.findall("joint")}
        self.assertEqual(set(joints), {"joint_1", "tool_mount"})
        rotation = joints["joint_1"]
        self.assertEqual(rotation.get("type"), "revolute")
        self.assertEqual(rotation.find("parent").get("link"), "base_link")
        self.assertEqual(rotation.find("child").get("link"), "arm_link")
        self.assertEqual(rotation.find("axis").get("xyz"), "0 0 1")
        mounting = joints["tool_mount"]
        self.assertEqual(mounting.get("type"), "fixed")
        self.assertEqual(mounting.find("parent").get("link"), "arm_link")
        self.assertEqual(mounting.find("child").get("link"), "tool")
        self.assertEqual(mounting.find("origin").get("xyz"), "0.2 0 0")
        hw = model.find("ros2_control")
        self.assertEqual(hw.findtext("hardware/plugin"), "mock_components/GenericSystem")
        joint = hw.find("joint")
        self.assertEqual(joint.get("name"), "joint_1")
        self.assertEqual([v.get("name") for v in joint.findall("command_interface")], ["position"])
        self.assertEqual([v.get("name") for v in joint.findall("state_interface")], ["position"])

    def test_controller_launch_and_installation(self):
        cfg = (LAB / "controllers.yaml").read_text(encoding="utf-8")
        launch = (LAB / "control.launch.py").read_text(encoding="utf-8")
        docker = (LAB / "Dockerfile").read_text(encoding="utf-8")
        ast.parse(launch)
        for part in ("update_rate: 50", "joint_state_broadcaster/JointStateBroadcaster",
                     "forward_command_controller/ForwardCommandController",
                     "interface_name: position", "joint_1"):
            self.assertIn(part, cfg)
        for part in ("robot_state_publisher", "ros2_control_node",
                     "spawner", "~/robot_description", "/robot_description",
                     "controllers.yaml", "arm.urdf"):
            self.assertIn(part, launch)
        for pkg in ("ros-${ROS_DISTRO}-ros2-control", "ros-${ROS_DISTRO}-ros2-controllers",
                    "ros-${ROS_DISTRO}-robot-state-publisher", "ros-${ROS_DISTRO}-tf2-ros"):
            self.assertIn(pkg, docker)
        for forbidden in ("gazebo", "rviz", "xfce", "vnc", "--privileged"):
            self.assertNotIn(forbidden, docker.lower())
        subprocess.run(["bash", "-n", str(LAB / "smoke_test.sh")],
                       check=True, capture_output=True)

    def test_joint_and_tool_pose(self):
        angle = 1.0
        self.assertAlmostEqual(0.2 * math.cos(angle), 0.10806046, places=7)
        self.assertAlmostEqual(0.2 * math.sin(angle), 0.16829420, places=7)
        self.assertAlmostEqual(math.degrees(angle), 57.2957795, places=5)

    def test_all_current_locales_have_self_contained_lab(self):
        self.assertGreaterEqual(len(LOCALES), 13)
        for lang in LOCALES:
            with self.subTest(lang=lang):
                page = ROOT / "docs" / lang / "notes" / "07-ros2-control-lab.md"
                text = page.read_text(encoding="utf-8")
                lesson = (ROOT / "docs" / lang / "notes" /
                          "06-ros2-foundations.md").read_text(encoding="utf-8")
                index = (ROOT / "docs" / lang / "README.md").read_text(encoding="utf-8")
                for marker in ("mock_components/GenericSystem", "/joint_states",
                               "/tf_static", "libsdformat14.so.14",
                               "LD_LIBRARY_PATH", "57.296", "1.0",
                               "ros2 topic pub --once", "robot_state_publisher",
                               "ros2_control_node", "transient_local",
                               "reliable", "0.108", "0.168", "NaN",
                               "../../../ros2/control_lab/README.md"):
                    self.assertIn(marker, text)
                self.assertIn("07-ros2-control-lab.md", lesson)
                self.assertIn("notes/07-ros2-control-lab.md", index)
                for other in LOCALES:
                    self.assertIn(f"../../{other}/notes/07-ros2-control-lab.md", text)
                self.assertNotIn("private", text.lower() if lang == "en" else "")

    def test_control_lab_never_reinstalls_in_completed_image(self):
        guide = (LAB / "README.md").read_text(encoding="utf-8")
        intro = guide.split("## 1. Build the image and open one shell", 1)[1].split(
            "## 2. Understand the files", 1)[0]
        self.assertIn("The control image's", intro)
        self.assertIn("at build time", intro)
        self.assertIn('source "/opt/ros/$ROS_DISTRO/setup.bash"', intro)
        self.assertIn("apt-get install -y ros-$ROS_DISTRO-ros2-control", intro)
        self.assertIn("Only for a separate bare Jazzy environment", intro)
        # The full guide exposes a clearly named session-local recovery section.
        self.assertIn("### Temporary recovery for a missing vendor library", guide)
        self.assertIn("ldd \"$plugin\" | grep 'not found'", guide)
        self.assertIn("ros2 launch /opt/control_lab/control.launch.py", guide)
        for lang in LOCALES:
            with self.subTest(lang=lang):
                page = (ROOT / "docs" / lang / "notes" /
                        "07-ros2-control-lab.md").read_text(encoding="utf-8")
                self.assertIn("dpkg-query -W ros-${ROS_DISTRO}-ros2-control", page)
                self.assertNotIn("apt-get install -y ros-$ROS_DISTRO-ros2-control", page)
                self.assertIn("#temporary-recovery-for-a-missing-vendor-library", page)

    def test_canonical_lab_explains_limitations(self):
        doc = (LAB / "README.md").read_text(encoding="utf-8")
        for marker in ("libgz-math7.so.7", "file core", "du -h core",
                       "ros2 control list_hardware_interfaces", "[claimed]",
                       "libsdformat14.so.14", "apt-get install libsdformat14",
                       "ros2 pkg executables controller_manager",
                       "hardware_spawner", "unspawner",
                       "NaN", "encoder", "0.108", "0.168"):
            self.assertIn(marker, doc)


if __name__ == "__main__":
    unittest.main()
