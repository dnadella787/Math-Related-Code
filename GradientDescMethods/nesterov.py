#!/usr/bin/python   

import math
import sys 

def gfunc3(v):
    return [math.log(v[0]), math.log(v[1])]
    #return [GRADIENT FUNC GOES HERE]


def vector_add(a, x, b, y):
    if (len(x) != len(y)):
        sys.stderr.write("ERROR: dimension mismatch in vector addition\n")
        exit(-1) 

    output = []
    for i in range(len(x)):
        output.append(a * x[i] + b * y[i])

    return output


class Nesterov:
    def __init__(self, x0, alpha, gf):
        self.x0 = x0
        self.alpha = alpha
        self.gf = gf

    def iterate(self, n):
        x = []
        x.append(self.x0)

        _lambda = list(range(n+2))
        _delta = list(range(n+1))

        y = []
        y.append(self.x0)

        for i in range(0,n+1):
            _lambda[i+1] = (1 + math.sqrt(1 + 4 * _lambda[i]**2))/2
            _delta[i] = (1 - _lambda[i]) / _lambda[i+1]
        
        print("Nesterov's Acceleration Method:")
        for i in range(1,n+1):
            y.append(vector_add(1, x[i-1], -1 * self.alpha, self.gf(x[i-1])))
            x.append(vector_add((1 - _delta[i-1]), y[i], _delta[i-1], y[i-1]))

            print("Iteration {0} :".format(i))
            print("Lambda_{0} : {1} and Delta_{2} : {3}".format(i, _lambda[i], i, _delta[i]))
            print("x_{0} : {1} and y_{2} : {3}\n".format(i, x[i], i, y[i]))

        return x[-1]


if __name__ == "__main__":
    N = Nesterov([10, 2], math.exp(1)-2, gfunc3)
    N.iterate(5)


            