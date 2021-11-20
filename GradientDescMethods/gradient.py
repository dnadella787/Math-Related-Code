#!/usr/bin/python
import math 
import sys

def gfunc3(v):
    return [math.log(v[0]), math.log(v[1])]
    #return [GRADIENT FUNC GOES HERE]

def vector_add(a, x, b, y):
    if (len(x) != len(y)):
        sys.stderr.write("ERROR: dimension mismatch btwn gradient and x_i\n")
        exit(-1) 

    output = []
    for i in range(len(x)):
        output.append(a * x[i] + b * y[i])

    return output
        


class Gradient:
    def __init__(self, x0, alpha, gf):
        self.x0 = x0
        self.alpha = alpha
        self.gf = gf

    def iterate(self, n):
        x = self.x0

        print("Gradient Descent Method:")
        print("x_0 : {0}".format(x))
        for i in range(n):
            x = vector_add(1, x, -1*self.alpha, self.gf(x))
            print("x{0} : {1}".format(i+1, x))

        print("\n")
        return x

if __name__ == "__main__":
    G = Gradient([10,2], math.exp(1)-2, gfunc3)
    G.iterate(5)


