# Program to make provided codes reusable by making them into functions

# Name: Matthew Bandama

# Student Number: BNDTAT003

# Date: 16-April-2014


def get_integer(a):
    
    if a == 'n':

        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
           
        return(n)
        
    elif a == 'k':
        
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        
        return(k)

def calc_factorial(n):

    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    
    return(nfactorial)

def calc_factorial (z):
    
    nkfactorial = 1
    for i in range (1, z+1):
        nkfactorial *= i
    
    return(nkfactorial)
