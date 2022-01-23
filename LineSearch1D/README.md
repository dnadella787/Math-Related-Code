This directory holds all the code for 1 dimensional line search methods used to find the minimum of a function.

There are 4 methods here and each one uses an object that needs to be initialized and then you call the function iterate(...) to actually generate output.

Example functions and how to actually call them are included in each file. (for example, func3)

1) Golden Section Method: (goldensection.py)

   This method uses same rho every iteration ((rho = 3-sqrt(5))/2)

   It has a class GoldenSection that can be initialized as:
             
             G = GoldenSection(a,b,f)

   where a is the start of the interval, b is the end of the interval, and f is the function
   being minimized. You can call iterate() now:

             G.iterate(n)

   where n is the number of iterations desired. Iterate returns the midpoint of the final interval but prints out the interval at each iteration where x* could possibly be.


2) Fibonacci Method: (fibonacci.py --> THIS PROGRAM NEEDS THE fib(..) METHOD AT THE TOP TO WORK)

   This method uses a different rho every iteration (rho_k = 1 - F_N-K/F_N+1-k)

   It has a class Fibonacci that can be initialized as:

             F = Fibonacci(a,b,f,epsilon)

   where a is the start of the interval, b is the end of the interval, f is the function
   being minimized, and epsilon is the amount to subtract from rho_N to keep it from being 1/2. You can call iterate() now:

             F.iterate(n)

   where n is the number of iterations desired. Iterate returns the midpoint of the final interval but prints out the interval at each iteration where x* could possibly be.

3) Bisection Method: (bisection.py)

   This method uses the derivative instead. 

   It has a class Bisection that can be initialized as:

             B = Bisection(a,b,df)

   where a is the start of the interval, b is the end of the interval, and df is the derivative of the function being minimized. You can call iterate() now:

             B.iterate(n)

   where n is the number of iterations desired. Iterate returns the midpoint of the final interval but prints out the interval at each iteration where x* could possibly be.

4) Newton's method: (newton.py)

   This is a little bit modified from Newton's actual method. Instead we use Newton's method to find the root of f'(x) and assuming unimodality, this gives the minimum of f itself. 

   It has a class called Newton that can be initialized as:

             N = Newton(df, df2)

   where df is the f'(x) and df2 is f''(x). Now iterate() can be called:

             N.iterate(x0,n)

   where x0 is the initial guess for the method and n is the number of iterations. Iterate will return the last x calculated within the given number of iterations.



There is also a bisection.cpp which is meant for the command line. To use this simply do:

   g++ bisection.cpp -o bisection
   ./bisection -a=-2 -b=0 -n=4 --function="2*x+cos(2*x)"

where a, b, n, and function are the left boundary, right boundary, number of intervals, and the function respectively. It also uses exprtk.hpp from this repo:

   https://github.com/ArashPartow/exprtk

which you will have to clone and then move exprtk.hpp into the same file. It is not a very flexible design right now but I am planning on producing my own math language parser soon when I have time which I can then release a big package. 

   