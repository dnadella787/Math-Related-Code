
import math

# CHANGE THIS FUNCTION TO RETURN A VECTOR OF LENGTH
# EQUAL TO THE NUMBER OF VARIABLES IN THE FUNCTION
# return the gradient of f (nabla f)
def func(x):
    return [2*x[0], math.exp(x[1])]

def alpha(x):
    return 0.01


def self_norm(g_i):
    output = 0
    for i in range(len(g_i)):
        output += g_i[i]**2
    
    return output 

def print_pair(vector):
    pair = "("
    for i in range(len(vector)):
        pair += str(vector[i]) + ", "
    return pair[0:-2]+")"

def add_vectors(a, v1, b, v2):
    if (len(v1) != len(v2)):
        print("ERROR: vectors are not of same length")
        exit(-1)
    
    output = [0] * len(v1)
    for i in range(len(v1)):
        output[i] = a * v1[i] + b * v2[i]

    return output

class CGD:
    def __init__(self, alpha, grad_func):
        self.alpha = alpha
        self.gradf = grad_func 
    

    def iterate(self, x0, n):
        x_i = x0 
        print("-----------------------------")
        print("x_{0} : ({1}, {2})".format(0, x_i[0], x_i[1]))
    
        d_i = [-1 * self.gradf(x0)[0], -1 * self.gradf(x0)[1]]
        g_i_1 = self.gradf(x_i)
        g_i = g_i_1
        b_i = 0

        for i in range(n):
            print("-----------------------------")

            x_i = add_vectors(1, x_i, self.alpha(1), d_i)
            print("x_{0} : {1}".format(i+1, print_pair(x_i)))

            g_i_1 = g_i
            g_i = self.gradf(x_i)
            # print("g_{0} : {1}".format(i+1,print_pair(g_i)))

            b_i = self_norm(g_i) / self_norm(g_i_1)
            # print("b_{0} :  {1}".format(i,b_i))

            d_i = add_vectors(-1, g_i, b_i, d_i)
            # print("d_{0} : {1}".format(i+1,print_pair(d_i)))

        print("-----------------------------")
        

if __name__ == "__main__":
    c = CGD(0.01, func)
    c.iterate([0,0],4)