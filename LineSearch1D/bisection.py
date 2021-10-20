import math

def dfunc3(x):
    return (2*x) + (math.cos(2*x))


class Bisection:
    def __init__(self, a, b, df):
        self.a = a
        self.b = b
        self.df = df


    def iterate(self,n):
        print("Bisection Method Data:\n")
        for i in range(n):
            c = self.a + (self.b - self.a)/2
            if self.df(c) > 0:
                self.b = c
            elif self.df(c) < 0:
                self.a = c 
            else:
                return c
            
            print("For iteration {0} the interval is [{1},{2}]".format(i+1,self.a,self.b))

        print("Interval of Uncertainty: [{0},{1}]\n".format(self.a, self.b))
        return self.a + (self.b - self.a)/2

if __name__ == "__main__":
    B = Bisection(-2,0,dfunc3)
    B.iterate(4)

