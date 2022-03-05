#include <iostream>
#include <math.h>
#include <argparser.h>
#include "fparser.h"

class bisection
{
protected:
    double a; 
    double b;
    std::string func_string; 

public:
    bisection(double l, double r, std::string f) : a(l), b(r), func_string(f) {}

    double iterate(int n)
    {
        fparser::fparser<double> fp(func_string, "x");
        std::cout << "\nBisection Method Data for " << func_string << " on [" << a << ", " << b << "]" << std::endl << std::endl;
        for (int i = 0; i < n; i++)
        {
            double c = a + (b - a)/2;
            double f = fp.calculate(c);
            if (f > 0)
                b = c;
            else if (f < 0)
                a = c;
            else
                return c;
        

            std::cout << "For iteration " << (i+1) << " the interval is [" << a << ", " << b << "]" << std::endl;
        }


        std::cout << std::endl << "Interval of Uncertainty : [" << a << ", " << b << "]" << std::endl;
        return a + (b-a)/2;
    }
};




int main(int argc, char* argv[])
{
    argparser::argument<ACTION::STORE> a("left boundary");
    a.set_flags("-a");
    a.set_help_message("left boundary (usage : -a [NUM] or -a=[NUM])");

    argparser::argument<ACTION::STORE> b("right boundary");
    b.set_flags("-b");
    b.set_help_message("right boundary (usage : -b [NUM] or -b=[NUM])");

    argparser::argument<ACTION::STORE> c("intervals");
    c.set_flags("-n");
    c.set_help_message("number of intervals (usage : -n [NUM] or -n=[NUM])");

    argparser::argument<ACTION::STORE> d("function");
    d.set_flags("--function", "-f");
    d.set_help_message("function to be optimized (usage : -f '[FUNCTION]' or --function '[FUNCTION]')");

    argparser::parser p;
    p.add_arguments(a, b, c, d);
    p.parse_args(argc, argv);

    int left = a.get<int>();
    int right = b.get<int>();
    int n = c.get<int>();

    std::string func = d.get<std::string>();

    bisection B(left, right, func);
    B.iterate(n);
}