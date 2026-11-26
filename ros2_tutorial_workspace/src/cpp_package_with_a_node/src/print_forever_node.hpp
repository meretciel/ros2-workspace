#pragma once

#include <memory>
#include <rclcpp/rclcpp.hpp>


class PrintForeverNode: public rclcpp::Node
{
private:
    double _timer_period;
    int _print_count;
    std::shared_ptr<rclcpp::TimerBase> _timer;

    void _timer_callback();

public:
    PrintForeverNode();
};