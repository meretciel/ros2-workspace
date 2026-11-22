import random
import rclpy
from rclpy.task import Future
from rclpy.node import Node

from package_with_interfaces.srv import WhatIsThePoint


class WhatIsThePointServiceClientNode(Node):
    def __init__(self):
        super().__init__('what_is_the_point_service_client')
        self.service_client = self.create_client(
            srv_type=WhatIsThePoint,
            srv_name="/what_is_the_point")

        while not self.service_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f"service {self.service_client.srv_name} is not available.")

        self.future: Future = None
        timer_period: float = 0.5
        self.timer = self.create_timer(
            timer_period_sec=timer_period,
            callback=self.timer_callback)


    def timer_callback(self):
        request = WhatIsThePoint.Request()
        if random.uniform(0, 1) < 0.5:
            request.quote.quote = "I wonder about Ultimate Question of Life."
            request.quote.philosopher_name = "Creators of Deep Thought"
            request.quote.id = 1979
        else:
            request.quote.quote = "It is always potatoes. I dream of potatoes."
            request.quote.philosopher_name = "a potato farmer"
            request.quote.id = 2013

        if self.future is not None and not self.future.done():
            self.future.cancel()
            self.get_logger("Service future cancelled. The node took too long to  process the service call.")

        self.future = self.service_client.call_async(request)
        self.future.add_done_callback(self.process_response)


    def process_response(self, future: Future):
        response = future.result()
        if response is not None:
            self.get_logger().info(f"Received a response: {response.point}")
        else:
            self.get_logger().info("Received a None response")

def main(args=None):
    try:
        rclpy.init(args=args)
        client_node = WhatIsThePointServiceClientNode()
        rclpy.spin(client_node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()


