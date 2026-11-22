import rclpy
from rclpy.node import Node
from package_with_interfaces.msg import AmazingQuote


class AmazingQuotePublisherNode(Node):
    """A ROS2 Node that publishes an amazing quote."""
    def __init__(self):
        super().__init__('amazing_quote_publisher_node')
        self.amazing_quote_publisher = self.create_publisher(
            msg_type=AmazingQuote,
            topic='/amazing_quote',
            qos_profile=1)
        timer_period: float = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.incremental_id: int = 0

    def timer_callback(self):
        amazing_quote = AmazingQuote()
        amazing_quote.id = self.incremental_id
        amazing_quote.quote = "Use the force, Pikachu!"
        amazing_quote.philosopher_name = "Uncle Ben"
        self.amazing_quote_publisher.publish(amazing_quote)
        self.incremental_id += 1

def main(args=None):
    try:
        rclpy.init(args=args)
        node = AmazingQuotePublisherNode()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
