#!/usr/bin/python3 




class Brahmagupta:
    def __init__(self, n):
        self.n = n 

    def calculate(self, x, y, k):
        if k == 1 and not x%1 and not y%1:
            return (x, y, k)

        while True:
            orig_x, x = x, x*x + self.n*y*y 
            y = orig_x * y + orig_x * y 
             
            x = abs(x/k)
            y = abs(y/k)
            k = 1 
            if not x%1 and not y%1:
                break 

        return (x, y, k)
        
    def give_multiple(self, first_sol, count):
        x, y, k = first_sol
        out = [first_sol]

        while len(out) < count:
            orig_x, x = x, x * x + self.n * y * y 
            y = orig_x * y + orig_x * y 
            out.append((x,y,k))

        return out 
        


if __name__ == "__main__":
    b = Brahmagupta(21)
    print(b.calculate(9,2,-3))
    # out = b.give_multiple(b.calculate(4,1,9), 3)


    # for x,y,k in out:
    #     if k == 1 and 1 == x*x - b.n * y * y:
    #         print(x,y,k)