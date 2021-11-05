These are the collection of all the conjugate gradient methods I've coded thus far.

So far there is Flether Reeves non-quadratic conjugate gradient descent method included here. It has support for functions in R^n given that you change the gradient function definition at the very top. 

    c = CGD(alpha, gradient_function)

where alpha is a function that returns the appropriate alpha at a given iteration and gradient function is the gradient of the function f.

    c.iterate([initial, ..., guess], n)

where [initial, ..., guess] is an array that represents the initial point to start at. If it was in R^2 and I wanted to start at (0, 0), I would use [0, 0]. n is the number of iterations to run for.

Uncomment print statements to get the other values for g_i (gradient of f at x_i), b_i (beta_i value using Fletcher Reeves), and d_i (the direction).