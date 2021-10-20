#!/usr/bin/python   

import math

def gfunc3(x):
    return math.log(x)

class Nesterov:
    def __init__(self, x0, gf):
        self.x0 = x0
        self.gf = gf

    def iterate(self, n):
        x = list(range(n+1))
        x[0] = self.x0

        _lambda = list(range(n+2))

        _delta = list(range(n+1))

        y = list(range(n+1))
        y[0] = self.x0

        for i in range(0,n+1):
            _lambda[i+1] = (1 + math.sqrt(1 + 4 * _lambda[i]**2))/2
            _delta[i] = (1 - _lambda[i]) / _lambda[i+1]
        
        print("Nesterov's Acceleration Method:")
        for i in range(1,n+1):
            y[i] = x[i-1] - (math.exp(1)-2) * (self.gf(x[i-1]))
            x[i] = (1 - _delta[i-1]) * y[i] + _delta[i-1] * y[i-1]

            print("Iteration {0}:".format(i))
            print("Lambda_{0}: {1} and Delta_{2}: {3}".format(i, _lambda[i], i, _delta[i]))
            print("x_{0}     : {1} and y_{2}    : {3}".format(i, x[i], i, y[i]))

        return x[-1]


if __name__ == "__main__":
    N = Nesterov(10, gfunc3)
    N.iterate(5)


            