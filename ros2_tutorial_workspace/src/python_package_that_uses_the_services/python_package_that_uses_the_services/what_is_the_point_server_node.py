import random

import rclpy
from rclpy.node import Node
from package_with_interfaces.srv import WhatIsThePoint

class WhatIsThePointServiceServerNode(Node):
    def __init__(self):
        super().__init__("what_is_the_point_service_server")

        self.service_server = self.create_service(
            srv_type=WhatIsThePoint,
            srv_name='/what_is_the_point',
            callback=self.what_is_the_point_service_callback)

        self.service_server_call_count: int = 0

    def what_is_the_point_service_callback(self,
                                           request: WhatIsThePoint.Request,
                                           response: WhatIsThePoint.Response
                                           ) -> WhatIsThePoint.Response:

        if "life" in request.quote.quote.lower():
            x = random.uniform(0, 42)
            y = random.uniform(0, 42)
            z = 42 - (x + y)
        else:
            x = random.uniform(0, 100)
            y = random.uniform(0, 100)
            z = random.uniform(0, 100)
            if x + y + z == 42:
                x += 1

        response.point.x = x
        response.point.y = y
        response.point.z = z

        self.service_server_call_count += 1

        self.get_logger().info(f"Quote: {request.quote.quote} || Name: {request.quote.philosopher_name}")

        return response


def main(args=None):
    try:
        rclpy.init(args=args)
        server_node = WhatIsThePointServiceServerNode()
        rclpy.spin(server_node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

