"""question 3
Michelle Lu
14 April 2014"""

import math #to be able to do the factorial
def get_integer(x):
    if x=="n": #when the parameter given is n
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        return n
    elif x=="k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)    
        return k
    
def calc_factorial(y):
    y=math.factorial(y) #calculate the factorial with the value of y
    return y