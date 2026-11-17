"""Check one editable ROS 2 architecture map and reciprocal localized navigation.

These offline checks inspect Mermaid source as text, not a rendered diagram or ROS runtime.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = tuple(sorted(x.name for x in (ROOT / "docs").iterdir() if x.is_dir()))
MAP = ROOT / "ros2" / "ROBOT_ARCHITECTURE.md"
NAMES = (
    "Perception",
    "Coordinate Transformation",
    "Motion Planning",
    "Motion Control",
    "Feedback",
)


class Ros2RobotArchitectureTests(unittest.TestCase):
    def test_one_mermaid_source_with_five_exact_functional_stages(self):
        doc = MAP.read_text(encoding="utf-8")
        diagrams = re.findall(r"```mermaid\n(.*?)\n```", doc, re.S)
        self.assertEqual(len(diagrams), 1)
        graph = diagrams[0]
        self.assertTrue(graph.startswith("flowchart LR"))
        stages = re.findall(
            r'^\s*subgraph\s+[A-Za-z_][A-Za-z_0-9]*\["([1-5])\. ([^"]+)"\]',
            graph, re.M,
        )
        self.assertEqual(stages, [(str(i), name) for i, name in enumerate(NAMES, 1)])
        self.assertEqual(graph.count("subgraph "), 5)
        self.assertIn("urdf[", graph)
        self.assertEqual(graph.count("urdf -.->"), 3)
        for input_name in ("image + acquisition timestamp", "camera_link",
                           "base_link", "FollowJointTrajectory action goal",
                           "state interfaces", "hardware", "/joint_states",
                           "/tf (moving)", "/tf_static (fixed)",
                           "robot_description", "local feedback"):
            with self.subTest(label=input_name):
                self.assertIn(input_name, graph)
        for arrow in (
            "camera -->", "detector -->", "tfbuf -->", "planner -->",
            "controller -->", "command -->", "servo -->", "motor -->",
            "encoder -->", "state -->", "broadcaster -->", "rsp -->",
            "encoder -->|\"local feedback\"| servo",
            "state -.->|\"controller read, not /joint_states\"| controller",
        ):
            with self.subTest(edge=arrow):
                self.assertIn(arrow, graph)
        self.assertNotIn("joint_trajectory_controller", graph.split(
            'subgraph MC["4. Motion Control"]', 1)[0])

    def test_reference_explains_roles_and_mock_limitations(self):
        doc = MAP.read_text(encoding="utf-8")
        for term in (
            "tf2_ros.Buffer.lookup_transform",
            "control_msgs/action/FollowJointTrajectory",
            "controller_manager", "hardware **command interfaces**",
            "hardware **state interfaces**",
            "robot_state_publisher", "joint_state_broadcaster",
            "forward_position_controller", "mock_components/GenericSystem",
            "local firmware loop", "not a runnable hardware system",
        ):
            with self.subTest(term=term):
                self.assertIn(term.lower(), doc.lower())
        self.assertLess(doc.index("**1. Perception**"),
                        doc.index("**5. Feedback**"))
        self.assertIn("The five numbered subgraphs", doc)
        self.assertIn("one Mermaid source block", doc)

    def test_every_language_has_own_explanation_and_navigation(self):
        common = MAP.read_text(encoding="utf-8")
        self.assertEqual(len(LOCALES), 13)
        for lang in LOCALES:
            with self.subTest(lang=lang):
                location = ROOT / "docs" / lang
                page = (location / "notes" /
                        "08-ros2-robot-architecture.md").read_text(encoding="utf-8")
                foundation = (location / "notes" /
                              "06-ros2-foundations.md").read_text(encoding="utf-8")
                control = (location / "notes" /
                           "07-ros2-control-lab.md").read_text(encoding="utf-8")
                index = (location / "README.md").read_text(encoding="utf-8")
                self.assertIn("08-ros2-robot-architecture.md", foundation)
                self.assertIn("08-ros2-robot-architecture.md", control)
                self.assertIn("notes/08-ros2-robot-architecture.md", index)
                self.assertIn("../../../ros2/ROBOT_ARCHITECTURE.md", page)
                self.assertIn(f"../docs/{lang}/notes/08-ros2-robot-architecture.md", common)
                self.assertNotIn("```mermaid", page)
                self.assertIn("URDF", page)
                self.assertIn("MoveIt 2", page)
                self.assertIn("forward_position_controller", page)
                self.assertIn("mock_components/GenericSystem", page)
                self.assertIn("/joint_states", page)
                self.assertIn("/tf_static", page)
                names = [page.index(f"**{i}. {name}**")
                         for i, name in enumerate(NAMES, 1)]
                self.assertEqual(names, sorted(names))
                for other in LOCALES:
                    link = ("08-ros2-robot-architecture.md" if other == lang
                            else f"../../{other}/notes/08-ros2-robot-architecture.md")
                    self.assertIn(link, page)

    def test_localized_stage_tables_have_three_columns(self):
        for lang in LOCALES:
            with self.subTest(lang=lang):
                page = (ROOT / "docs" / lang / "notes" /
                        "08-ros2-robot-architecture.md").read_text(encoding="utf-8")
                rows = [line for line in page.splitlines() if line.startswith("| ")]
                self.assertEqual(len(rows), 7)
                self.assertTrue(all(row.count("|") == 4 for row in rows))
                self.assertEqual(rows[1], "| --- | --- | --- |")
                for number, name in enumerate(NAMES, 1):
                    self.assertIn(f"| **{number}. {name}** |", rows[number + 1])
                if lang != "en":
                    self.assertNotIn("**Languages:**", page)
                    self.assertNotIn("[ROS 2 foundations]", page)
                    self.assertNotIn("[Open and edit the single Mermaid architecture diagram]", page)

    def test_repository_exposes_the_diagram_without_private_state(self):
        for path in ("README.md", "ros2/README.md", "ros2/control_lab/README.md",
                     "AGENTS.md", "MAINTENANCE.md"):
            with self.subTest(path=path):
                self.assertIn("ROBOT_ARCHITECTURE.md",
                              (ROOT / path).read_text(encoding="utf-8"))
        self.assertIn("08-ros2-robot-architecture.md",
                      (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn("Perception, Coordinate Transformation, Motion Planning, Motion Control, Feedback",
                      (ROOT / "AGENTS.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
