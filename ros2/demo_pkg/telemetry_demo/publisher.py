"""Publish a synthetic sequence; no robot or device control."""
import math

import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from std_msgs.msg import String


class SampleSource(Node):
    def __init__(self):
        super().__init__('sample_source')
        self.declare_parameter('interval_s', 1.0)
        period = float(self.get_parameter('interval_s').value)
        if not math.isfinite(period) or period <= 0.0:
            raise ValueError('interval_s must be finite and positive')
        self.publisher = self.create_publisher(String, '/training/status', 10)
        self.sequence = 0
        self.timer = self.create_timer(period, self.publish_sample)

    def publish_sample(self):
        self.sequence += 1
        message = String()
        message.data = f'sample {self.sequence}'
        self.publisher.publish(message)
        self.get_logger().info(f'published: {message.data}')


def main(args=None):
    rclpy.init(args=args)
    node = None
    try:
        node = SampleSource()
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        if node is not None:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
