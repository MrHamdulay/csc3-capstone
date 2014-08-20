#module to calculate factorial
#Runako muzwidzwa MZWRUN001
#15 april 2014
def get_integer (c):
    n = input ("Enter "+c+":\n")
    while not n.isdigit ():
        n = input ("Enter "+c+":\n")
    n = eval (n)   
    return n
    
def calc_factorial(x):
    nfactorial = 1
    for i in range (1, x+1):
        nfactorial *= i
    return nfactorial
  
    
