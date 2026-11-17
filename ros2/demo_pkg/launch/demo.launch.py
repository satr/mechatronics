"""Launch both simulation-only processes in the same ROS 2 graph."""
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='telemetry_demo',
            executable='sample_source',
            output='screen',
            parameters=[{'interval_s': 1.0}],
        ),
        Node(
            package='telemetry_demo',
            executable='sample_monitor',
            output='screen',
        ),
    ])
