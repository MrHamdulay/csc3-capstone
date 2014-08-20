#module calculating number of k-permutations of n numbers
#CLLCAM003 
#15/04/2014

def get_integer(x):
    y = input ("Enter "+x+":\n")
    while not y.isdigit ():
        y = input ("Enter "+x+":\n")
    x = eval (y)
    return x
    
   

def calc_factorial(x):
    xfactorial = 1
    for i in range (1, x+1):
        xfactorial *= i
    return xfactorial
    