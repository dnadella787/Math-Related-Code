Code for gradient descent and Nesterov's acceleration (also called Nesterov's momentum/NAG) in R^n here. 

Similar to 1DLineSearch this uses classes with an iterate() function.

1) Gradient Descent Method: (gradient.py)

   The class can be initialized as:

             G = Gradient(x0, alpha, gf)

   where x0 is the initial guess, alpha is another constant for you to choose, and gf is the gradient function. Note, if gf is L-Lipschitz continuous then alpha is likely 1/L. Now you can call the iterate() function:

             G.iterate(n)

   where n is the number of iterations. iterate() returns the final x calculated but also prints out the x calculated at each iteration.

2) Nesterov's Acceleration (nesterov.py)

   The class can be initialized as:

             N = Nesterov(x0, alpha, gf) 

   where x0 is the initial guess, alpha is a constant, and gf is the gradient function. You can call the iterate() function now:

             N.iterate(n)

   where n is the number of iterations to be done. iterate() returns the final x value calculated but also prints out each x_k, y_k, lambda_k, and delta_k at each kth iteration. 

   