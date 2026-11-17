"""Count synthetic topic messages and expose a read-only Trigger service."""
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from std_msgs.msg import String
from std_srvs.srv import Trigger


class SampleMonitor(Node):
    def __init__(self):
        super().__init__('sample_monitor')
        self.count = 0
        self.subscription = self.create_subscription(
            String, '/training/status', self.receive_sample, 10)
        self.service = self.create_service(
            Trigger, '/training/count', self.report_count)

    def receive_sample(self, message):
        self.count += 1
        self.get_logger().info(f'received: {message.data} (count={self.count})')

    def report_count(self, request, response):
        response.success = True
        response.message = f'received {self.count} samples'
        return response


def main(args=None):
    rclpy.init(args=args)
    node = None
    try:
        node = SampleMonitor()
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
