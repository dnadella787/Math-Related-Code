#!/usr/bin/python
import math 

def gfunc3(x):
    return math.log(x)


class Gradient:
    def __init__(self, x0, alpha, gf):
        self.x0 = x0
        self.alpha = alpha
        self.gf = gf

    def iterate(self, n):
        x = self.x0

        print("Gradient Descent Method:")
        for i in range(n):
            x -= self.alpha * self.gf(x)
            print("x{0} : {1}".format(i+1, x))

        print("\n")
        return x

if __name__ == "__main__":
    G = Gradient(10, math.exp(1)-2, gfunc3)
    G.iterate(5)


