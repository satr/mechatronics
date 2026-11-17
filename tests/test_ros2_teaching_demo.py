"""Offline structure and behavioral tests for the synthetic ROS 2 demo.

These fakes exercise application callbacks; they do NOT validate DDS, Docker,
the actual rclpy runtime, or real-time behavior on a robot.
"""
import ast
import importlib.util
import re
import subprocess
import sys
import types
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(path.name for path in (ROOT / "docs").iterdir() if path.is_dir()))
PACKAGE = ROOT / "ros2" / "demo_pkg"
SOURCES = PACKAGE / "telemetry_demo"


class FakeNode:
    def __init__(self, name):
        self.node_name = name
        self.sent = []
        self.received_callback = None
        self.service_callback = None
        self.period = None

    def declare_parameter(self, name, default):
        assert name == "interval_s" and default == 1.0

    def get_parameter(self, name):
        assert name == "interval_s"
        return SimpleNamespace(value=1.0)

    def create_publisher(self, message_type, name, depth):
        assert name == "/training/status" and depth == 10
        return SimpleNamespace(publish=lambda message: self.sent.append(message.data))

    def create_subscription(self, message_type, name, callback, depth):
        assert name == "/training/status" and depth == 10
        self.received_callback = callback
        return callback

    def create_service(self, service_type, name, callback):
        assert name == "/training/count"
        self.service_callback = callback
        return callback

    def create_timer(self, period, callback):
        self.period = period
        return callback

    def get_logger(self):
        return SimpleNamespace(info=lambda message: None)


class FakeString:
    def __init__(self):
        self.data = ""


def load_with_fake_ros(name, path):
    rclpy = types.ModuleType("rclpy")
    rclpy.node = types.ModuleType("rclpy.node")
    rclpy.node.Node = FakeNode
    rclpy.executors = types.ModuleType("rclpy.executors")
    rclpy.executors.ExternalShutdownException = type("ExternalShutdownException", (Exception,), {})
    std_msgs = types.ModuleType("std_msgs")
    std_msgs.msg = types.ModuleType("std_msgs.msg")
    std_msgs.msg.String = FakeString
    std_srvs = types.ModuleType("std_srvs")
    std_srvs.srv = types.ModuleType("std_srvs.srv")
    std_srvs.srv.Trigger = type("Trigger", (), {})
    mocks = {
        "rclpy": rclpy, "rclpy.node": rclpy.node,
        "rclpy.executors": rclpy.executors,
        "std_msgs": std_msgs, "std_msgs.msg": std_msgs.msg,
        "std_srvs": std_srvs, "std_srvs.srv": std_srvs.srv,
    }
    with patch.dict(sys.modules, mocks):
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    return module


class Ros2ChapterChecks(unittest.TestCase):
    def test_all_supported_locales_have_complete_navigation(self):
        for locale in LOCALES:
            with self.subTest(locale=locale):
                path = ROOT / "docs" / locale / "notes" / "06-ros2-foundations.md"
                text = path.read_text(encoding="utf-8")
                self.assertGreater(len(text), 5500)
                self.assertEqual(
                    [int(n) for n in re.findall(r'<a id="section-(\d+)"></a>', text)],
                    list(range(1, 13)))
                for diagram in ("ros2-topic-service.svg", "ros2-software-layers.svg"):
                    self.assertIn(diagram, text)
                for token in ("ros2_control", "URDF", "tf2", "DDS", "QoS",
                              "colcon", "ros2 node list", "ros2 service call",
                              "ros2 action list", "docker compose"):
                    self.assertIn(token, text)
                for other in LOCALES:
                    target = ("06-ros2-foundations.md" if other == locale
                              else f"../../{other}/notes/06-ros2-foundations.md")
                    self.assertIn(f"]({target})", text)
                index = (ROOT / "docs" / locale / "README.md").read_text(encoding="utf-8")
                self.assertIn("13. [", index)
                self.assertIn("(notes/06-ros2-foundations.md)", index)

    def test_maintainer_docs_match_supported_locales_and_asset_licenses(self):
        """Prevent misleading contributor instructions and ambiguous SVG licensing."""
        for name in ("AGENTS.md", "CONTRIBUTING.md", "WRITING_STYLE.md"):
            with self.subTest(name=name):
                text = (ROOT / name).read_text(encoding="utf-8").lower()
                self.assertNotIn("all ten editions", text)
                self.assertNotIn("all nine translations", text)
                self.assertNotIn("all ten language editions", text)
        license_text = (ROOT / "LICENSING.md").read_text(encoding="utf-8")
        self.assertIn("assets/figures/", license_text)
        self.assertIn("Apache-2.0", license_text)
        self.assertIn("Third-party", license_text)
        for asset in ("ros2/demo_pkg/", "ros2/Dockerfile", "ros2/compose.yaml"):
            self.assertIn(asset, license_text)
        self.assertIn("ros2/smoke_test.sh", license_text)

    def test_original_diagrams_parse(self):
        for name in ("ros2-topic-service.svg", "ros2-software-layers.svg"):
            path = ROOT / "assets" / "figures" / name
            root = ET.parse(path).getroot()
            self.assertTrue(root.tag.endswith("svg"))
            self.assertIn("viewBox", root.attrib)
            self.assertNotIn("<script", path.read_text(encoding="utf-8").lower())

    def test_package_and_launch(self):
        root = ET.parse(PACKAGE / "package.xml").getroot()
        self.assertEqual(root.findtext("name"), "telemetry_demo")
        self.assertEqual(root.findtext("license"), "Apache-2.0")
        self.assertIn("license=\'Apache-2.0\'", (PACKAGE / "setup.py").read_text(encoding="utf-8"))
        self.assertEqual(root.findtext("export/build_type"), "ament_python")
        deps = {item.text for item in root.findall("exec_depend")}
        self.assertTrue({"rclpy", "std_msgs", "std_srvs", "launch", "launch_ros"} <= deps)
        for path in (PACKAGE / "setup.py", PACKAGE / "launch" / "demo.launch.py",
                     SOURCES / "publisher.py", SOURCES / "subscriber.py"):
            with self.subTest(path=str(path)):
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        setup = (PACKAGE / "setup.py").read_text(encoding="utf-8")
        launch = (PACKAGE / "launch" / "demo.launch.py").read_text(encoding="utf-8")
        self.assertIn("sample_source = telemetry_demo.publisher:main", setup)
        self.assertIn("sample_monitor = telemetry_demo.subscriber:main", setup)
        self.assertIn("launch/demo.launch.py", setup)
        self.assertEqual(launch.count("Node("), 2)
        docker = (ROOT / "ros2" / "Dockerfile").read_text(encoding="utf-8")
        compose = (ROOT / "ros2" / "compose.yaml").read_text(encoding="utf-8")
        self.assertIn("FROM ros:jazzy-ros-base", docker)
        self.assertIn("colcon build --packages-select telemetry_demo", docker)
        self.assertIn('ROS_DOMAIN_ID: "42"', compose)
        self.assertNotIn("privileged:", compose)
        self.assertNotIn("network_mode: host", compose)

    def test_official_demo_packages_and_interactive_learning_order(self):
        """Built-in demos precede the source-built package; source once per shell."""
        docker = (ROOT / "ros2" / "Dockerfile").read_text(encoding="utf-8")
        guide = (ROOT / "ros2" / "README.md").read_text(encoding="utf-8")
        for name in ("ros-${ROS_DISTRO}-demo-nodes-cpp", "ros-${ROS_DISTRO}-demo-nodes-py"):
            self.assertIn(name, docker)
        for token in ("ros2 run demo_nodes_cpp talker",
                      "ros2 run demo_nodes_py listener",
                      "colcon build --packages-select telemetry_demo",
                      "docker compose exec demo bash",
                      "source /opt/ros/${ROS_DISTRO}/setup.bash",
                      "source /opt/training_ws/install/setup.bash",
                      "control_lab/README.md"):
            if token == "colcon build --packages-select telemetry_demo":
                self.assertIn(token, docker)
            else:
                self.assertIn(token, guide)
        # Single-command prefixes are for automation; ordinary reader commands
        # should not repeat a fresh source chain on every line.
        self.assertNotIn("docker compose exec demo bash -lc", guide)
        self.assertIn("docker compose exec -T demo bash -lc", guide)
        self.assertIn("Dockerfile `RUN`", guide)
        self.assertIn("container's `CMD`", guide)

    def test_all_locale_practical_ros_sections_use_one_interactive_shell(self):
        for lang in LOCALES:
            with self.subTest(lang=lang):
                document = (ROOT / "docs" / lang / "notes" /
                            "06-ros2-foundations.md").read_text(encoding="utf-8")
                section = document.split('<a id="section-11"></a>', 1)[1].split(
                    '<a id="section-12"></a>', 1)[0]
                self.assertIn("demo_nodes_cpp", section)
                self.assertIn("demo_nodes_py", section)
                self.assertIn("telemetry_demo", section)
                self.assertIn("docker compose exec demo bash", section)
                self.assertNotIn("docker compose exec demo bash -lc", section)
                for command in ('echo "$ROS_DISTRO"', "ros2 node list", "ros2 service call"):
                    self.assertIn(command, section)

    def test_docker_smoke_script_syntax_and_scope(self):
        """Offline validation checks syntax; the separate live workflow exercises ROS."""
        script = ROOT / "ros2" / "smoke_test.sh"
        content = script.read_text(encoding="utf-8")
        subprocess.run(["bash", "-n", str(script)], check=True, capture_output=True)
        for required in ("docker compose up --build -d", "ros2 node list",
                         "ros2 topic echo --once", "ros2 service call",
                         "ros2 service list", "timeout 12s", "timeout 4s",
                         "deadline=$((SECONDS + 60))", "set -euo pipefail",
                         "received [1-9][0-9]* samples"):
            self.assertIn(required, content)
        self.assertNotIn("privileged", content)
        self.assertNotIn("network_mode: host", content)
        instructions = (ROOT / "ros2" / "README.md").read_text(encoding="utf-8")
        self.assertIn("bash ros2/smoke_test.sh", instructions)
        self.assertIn("script has been executed by the live GitHub Actions workflow", instructions)

    def test_live_ros_workflow_is_real_and_scoped(self):
        """The live smoke check is separate from the fast offline validation job."""
        workflow = (ROOT / ".github" / "workflows" / "ros2-live-smoke.yml").read_text(encoding="utf-8")
        self.assertIn("branches: [main]", workflow)
        self.assertNotIn("pull_request:", workflow)
        self.assertIn("if: github.ref == 'refs/heads/main'", workflow)
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("ros2/**", workflow)
        self.assertIn("bash ros2/smoke_test.sh", workflow)
        self.assertIn("if: always()", workflow)
        self.assertIn("docker compose -f ros2/compose.yaml down", workflow)

    def test_publisher_rejects_nonfinite_or_nonpositive_intervals(self):
        publisher = load_with_fake_ros("ros_demo_pub_interval_test", SOURCES / "publisher.py")
        for interval in (0.0, -0.1, float("nan"), float("inf"), float("-inf")):
            with self.subTest(interval=interval):
                with patch.object(FakeNode, "get_parameter",
                                  return_value=SimpleNamespace(value=interval)):
                    with self.assertRaisesRegex(ValueError, "finite and positive"):
                        publisher.SampleSource()

    def test_message_callbacks_without_ros_runtime(self):
        publisher = load_with_fake_ros("ros_demo_pub_test", SOURCES / "publisher.py")
        subscriber = load_with_fake_ros("ros_demo_sub_test", SOURCES / "subscriber.py")
        source = publisher.SampleSource()
        monitor = subscriber.SampleMonitor()
        self.assertEqual(source.node_name, "sample_source")
        self.assertEqual(monitor.node_name, "sample_monitor")
        self.assertEqual(source.period, 1.0)
        source.publish_sample()
        source.publish_sample()
        self.assertEqual(source.sent, ["sample 1", "sample 2"])
        response = SimpleNamespace(success=None, message=None)
        monitor.report_count(None, response)
        self.assertEqual((response.success, response.message), (True, "received 0 samples"))
        for payload in source.sent:
            monitor.receive_sample(SimpleNamespace(data=payload))
        response = SimpleNamespace(success=None, message=None)
        monitor.report_count(None, response)
        self.assertEqual((response.success, response.message), (True, "received 2 samples"))


if __name__ == "__main__":
    unittest.main()
