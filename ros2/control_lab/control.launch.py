"""Headless Jazzy one-joint mock: URDF -> ros2_control -> /joint_states -> tf2.

The launch description uses source paths directly, not an installed ROS package.
No Gazebo, RViz, physical drivers or external services are required.
"""
from pathlib import Path

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    here = Path(__file__).resolve().parent
    robot_description = (here / "arm.urdf").read_text(encoding="utf-8")
    controllers = str(here / "controllers.yaml")

    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            output="screen",
            parameters=[{"robot_description": robot_description}],
        ),
        Node(
            package="controller_manager",
            executable="ros2_control_node",
            name="controller_manager",
            output="screen",
            parameters=[controllers],
            remappings=[("~/robot_description", "/robot_description")],
        ),
        Node(
            package="controller_manager",
            executable="spawner",
            name="spawner_joint_state_broadcaster",
            output="screen",
            arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
        ),
        Node(
            package="controller_manager",
            executable="spawner",
            name="spawner_forward_position_controller",
            output="screen",
            arguments=["forward_position_controller", "--controller-manager", "/controller_manager"],
        ),
    ])
