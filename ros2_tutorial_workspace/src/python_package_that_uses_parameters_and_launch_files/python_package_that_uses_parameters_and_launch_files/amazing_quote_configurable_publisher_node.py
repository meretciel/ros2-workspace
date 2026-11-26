import rclpy
from rclpy.node import Node
from package_with_interfaces.msg import AmazingQuote


class AmazingQuoteConfigurablePublisherNode(Node):
    def __init__(self):
        super().__init__("amazing_quote_configurable_publisher_node")
        self.declare_parameter("quote", "Use the force, Pikachu!")
        self.declare_parameter("philosopher_name", "Uncle Ben")

        self.declare_parameter("topic_name", "amazing_quote")
        topic_name = self.get_parameter("topic_name").get_parameter_value().string_value
        self.declare_parameter("period", 0.5)
        timer_period = self.get_parameter("period").get_parameter_value().double_value

        self.publisher = self.create_publisher(
            msg_type=AmazingQuote,
            topic=topic_name,
            qos_profile=1
        )

        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.incremental_id = 0

    def timer_callback(self):
        quote_value = self.get_parameter("quote").get_parameter_value().string_value
        philosopher_name = self.get_parameter("philosopher_name").get_parameter_value().string_value
        quote = AmazingQuote()
        quote.id = self.incremental_id
        quote.quote = quote_value
        quote.philosopher_name = philosopher_name

        self.publisher.publish(quote)
        self.incremental_id += 1


def main(args=None):
    try:
        rclpy.init(args=args)
        publisher_node = AmazingQuoteConfigurablePublisherNode()
        rclpy.spin(publisher_node)
    except KeyboardInterrupt:
        pass

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

