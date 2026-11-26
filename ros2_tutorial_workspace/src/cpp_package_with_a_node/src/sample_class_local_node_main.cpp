#include <rclcpp/rclcpp.hpp>
#include "cpp_package_with_a_library/sample_class_local_node.hpp"

int main(int argc, char** argv)
{
    rclcpp::init(argc,argv);
    try
    {
        auto node = std::make_shared<SampleClassLocalNode>();
        rclcpp::spin(node);
    }
    catch (const std::exception& e)
    {
        std::cerr << std::string("::Exception::") << e.what();
    }
    return 0;
}