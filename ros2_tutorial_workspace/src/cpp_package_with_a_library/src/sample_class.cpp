#include <sstream>
#include "cpp_package_with_a_library/sample_class.hpp"


SampleClass::SampleClass()
{
}

int SampleClass::get_a_private_member() const
{
    return a_private_member_;
}

void SampleClass::set_a_private_member(int value)
{
    a_private_member_ = value;
}

double SampleClass::sum_of_squares(const double &a, const double &b)
{
    return a*a + 2*a*b + b*b;
}

std::string SampleClass::to_string() const
{
    std::stringstream ss;
    ss << "Sample_Class:: " << std::endl <<
          "a_private_member_ = "        << std::to_string(a_private_member_) << std::endl;
    return ss.str();
}

std::ostream &operator<<(std::ostream &os, const SampleClass &sc)
{
    return os << sc.to_string();
}