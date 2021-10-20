import math

def func3(x):
    return (x**2) + (math.cos(x) * math.sin(x))


# def func4(x):
#     return (x**4) - 14 * (x**3) + 60 * (x**2) - 70 * x

class GoldenSection:
    def __init__(self, a, b, f):
        self.a = a
        self.b = b
        self.f = f


    def iterate(self,n):
        print("Golden Section Data:\n")
        rho = (3-math.sqrt(5))/2
        for i in range(n):
            c = self.a + rho * (self.b - self.a) 
            d = self.b - rho * (self.b - self.a)
            if (self.f(c) > self.f(d)):
                self.a = c
            else:
                self.b = d

            print("For iteration {0} the interval is [{1},{2}]".format(i+1,self.a,self.b))
            

        print("Interval of Uncertainty: [{0},{1}]\n".format(self.a, self.b))
        return self.a + (self.b - self.a)/2

if __name__ == "__main__":
    G = GoldenSection(-2,0,func3)
    G.iterate(4)

    
