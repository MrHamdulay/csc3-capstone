import math


        

                
def get_integer(c):
        if c =="k":
                k = input ("Enter k:\n")
                while not k.isdigit ():
                        k = input ("Enter k:\n")
                k = eval (k)                    
                return k
        else:
                n = input ("Enter n:\n")
                while not n.isdigit ():
                        n = input ("Enter n:\n")
                n = eval (n)                   
                return n

def calc_factorial(v):
        return math.factorial(v)