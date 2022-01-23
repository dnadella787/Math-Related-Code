#include <iostream>
#include <math.h>
#include "exprtk.hpp"
#include <argparser.h>

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
        std::cout << "\nBisection Method Data for " << func_string << " on [" << a << ", " << b << "]" << std::endl << std::endl;
        for (int i = 0; i < n; i++)
        {
            double c = a + (b - a)/2;
            if (f(c) > 0)
                b = c;
            else if (f(c) < 0)
                a = c;
            else
                return c;
        

            std::cout << "For iteration " << (i+1) << " the interval is [" << a << ", " << b << "]" << std::endl;
        }


        std::cout << std::endl << "Interval of Uncertainty : [" << a << ", " << b << "]" << std::endl;
        return a + (b-a)/2;
    }

    double f(double x)
    {
        typedef exprtk::symbol_table<double> symbol_table_t;
        typedef exprtk::expression<double>   expression_t;
        typedef exprtk::parser<double>       parser_t;

        const std::string expression_string = func_string;


        symbol_table_t symbol_table;
        symbol_table.add_variable("x",x);
        symbol_table.add_constants();

        expression_t expression;
        expression.register_symbol_table(symbol_table);

        parser_t parser;
        parser.compile(expression_string,expression);


        return expression.value();
    }

};




int main(int argc, char* argv[])
{
    argument a("left boundary");
    a.set_flags("-a");
    a.set_help_message("left boundary");
    a.set_action(STORE);

    argument b("right boundary");
    b.set_flags("-b");
    b.set_help_message("right boundary");
    b.set_action(STORE);

    argument c("intervals");
    c.set_flags("-n");
    c.set_help_message("number of intervals");
    c.set_action(STORE);

    argument d("function");
    d.set_flags("--function", "-f");
    d.set_help_message("function to be optimized");
    d.set_action(STORE);

    parser p;
    p.add_arguments(&a, &b, &c, &d);
    p.parse_args(argc, argv);

    int left = std::stod(a.get_store());
    int right = std::stod(b.get_store());
    int n = std::stod(c.get_store());
    std::string func = d.get_store();

    bisection B(left, right, func);
    B.iterate(n);
}