#pragma once

#include <rclcpp/rclcpp.hpp>
#include <cpp_package_with_a_library/sample_class.hpp>

/**
 * @brief A ROS2 Node that uses the SampleClass within the same package.
 */
class SampleClassLocalNode: public rclcpp::Node
{
private:
    SampleClass sample_class_;

    double timer_period_;
    int print_count_;
    rclcpp::TimerBase::SharedPtr timer_;

    void _timer_callback();
public:
    SampleClassLocalNode();

};