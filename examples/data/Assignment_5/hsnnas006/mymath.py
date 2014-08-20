#mymath
#by nasreen
import math
#function to get integer from user
def get_integer(x):
    s = input ("Enter "+ str(x)+ ":\n")
    while not s.isdigit():
        s = input ("Enter "+ str(x)+ ":\n")   
    s = eval(s)
        
    return s

#function to calculate factorial
def calc_factorial(b):
    nfactorial = 1
    for i in range(1, b+1):
        nfactorial *= i
    return nfactorial  #returns factorial
    
  