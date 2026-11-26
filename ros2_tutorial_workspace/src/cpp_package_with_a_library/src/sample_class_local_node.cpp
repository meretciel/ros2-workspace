#include "cpp_package_with_a_library/sample_class_local_node.hpp"


SampleClassLocalNode::SampleClassLocalNode():
    rclcpp::Node("sample_class_local_node"),
    timer_period_(0.5),
    print_count_(0)
{
    timer_ = create_wall_timer(
                std::chrono::milliseconds(long(timer_period_*1e3)),
                std::bind(&SampleClassLocalNode::_timer_callback, this)
                );
}

void SampleClassLocalNode::_timer_callback()
{
    RCLCPP_INFO_STREAM(get_logger(),
                       std::string("sum_of_squares = ") +
                       std::to_string(SampleClass::sum_of_squares(print_count_,print_count_-5))
                       );

    RCLCPP_INFO_STREAM(get_logger(),
                       sample_class_.to_string() +
                       std::to_string(print_count_) +
                       std::string(" times.")
                       );
    print_count_++;
}