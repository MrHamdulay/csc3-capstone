from mymath import *

def get_integer(var_name):
    n = input ("Enter " + var_name + ":\n")
    while not n.isdigit ():
       n = input ("Enter " + var_name + ":\n")
    n = eval (n)
    return n
    
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial