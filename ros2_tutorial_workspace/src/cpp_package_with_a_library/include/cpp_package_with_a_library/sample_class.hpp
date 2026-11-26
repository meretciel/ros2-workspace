#pragma once

#include <ostream>



class SampleClass
{
private:
    int a_private_member_;

public:
    SampleClass();

    int get_a_private_member() const;
    void set_a_private_member(int value);
    std::string to_string() const;

    static double sum_of_squares(const double&a, const double& b);
};

std::ostream& operator<<(std::ostream& os, const SampleClass& sc);