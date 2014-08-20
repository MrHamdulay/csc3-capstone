"""Module that helps in calculating factorials
Author: Pankaj Munbodh
16 April 2014"""

#Ask user for input that depends on parameter a
def get_integer(a):
    n=input("Enter"+" "+a+":\n")
    while not n.isdigit ():
        n=input("Enter"+" "+a+":\n")
    n=eval(n)
    return n

# calculates factorial of a number
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
       nfactorial *= i
       
    return nfactorial

    
    
    
    
    
