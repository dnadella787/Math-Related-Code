import math

def dfunc3(x):
    return (2*x) + (math.cos(2*x))

def d2func3(x):
    return 2 - 2*math.sin(2*x)


class Newton:
    def __init__(self, df, df2):
        self.df = df
        self.df2 = df2


    def iterate(self,x0,n):
        x = x0
        for i in range(n):
            print("x{0} : {1}".format(i, x))
            x -= self.df(x)/self.df2(x)
            
        print("x{0} : {1}".format(n, x))
        return x 

if __name__ == "__main__":
    G = Newton(dfunc3,d2func3)
    G.iterate(-1,10)

