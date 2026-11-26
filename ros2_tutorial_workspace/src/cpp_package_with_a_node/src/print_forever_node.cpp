#include "print_forever_node.hpp"

PrintForeverNode::PrintForeverNode():
    rclcpp::Node("print_forever_node"),
    _timer_period(0.5),
    _print_count(0)

{
    _timer = create_wall_timer(
                std::chrono::milliseconds(long(_timer_period * 1e3)),
                std::bind(&PrintForeverNode::_timer_callback, this)
    );
}


void PrintForeverNode::_timer_callback()
{
    RCLCPP_INFO_STREAM(get_logger(),
                       std::string("Printed ") +
                       std::to_string(_print_count) +
                       std::string(" times."));
    _print_count++;
}