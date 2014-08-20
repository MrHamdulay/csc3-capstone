#module with functions to calculate number of k-permutations of n numbers
#joshua gullan 
#16 april 2014

def get_integer(x):
    s = input ("Enter "+x+":\n")
    while not s.isdigit ():
        s = input ("Enter "+x+":\n")
    x = eval (s)
    return x
    
   

def calc_factorial(x):
    xfactorial = 1
    for i in range (1, x+1):
        xfactorial *= i
    return xfactorial
    