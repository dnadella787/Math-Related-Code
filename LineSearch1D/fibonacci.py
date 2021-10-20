import math


def fib(n):
    if n == -1:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def func3(x):
    return (x**2) + (math.cos(x) * math.sin(x))


class Fibonacci:
    def __init__(self, a, b, f, epsilon):
        self.a = a
        self.b = b
        self.f = f
        self.epsilon = epsilon


    def iterate(self,n):
        print("Fibonacci Method Data:\n")
        for i in range(n):
            if i == n-1:
                rho = (1-(fib(n-i)/fib(n+1-i))) - self.epsilon
            else:
                rho = (1-(fib(n-i)/fib(n+1-i)))

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
    F = Fibonacci(-2,0,func3,0.05)
    F.iterate(4)

