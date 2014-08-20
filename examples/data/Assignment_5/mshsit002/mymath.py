#Programme that caculates the factorial and number of arrangements
# Author: Sithembiso
# 15 April 2014

def get_integer(parameter):
   
    
    #
    if parameter == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")#this will happen until the user print a natural number 
        n = eval (n)
        return n
      
    # asking the user for k items arrangements 
    elif parameter =="k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)   
        return k
    
def calc_factorial(x):

    
   
    nfactorial = 1
    
    
    for i in range (1, x+1):
        nfactorial *= i    
    return nfactorial
    
    
