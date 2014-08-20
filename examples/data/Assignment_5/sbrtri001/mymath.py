# Assignment 5, question 3
# Tristan Subroyen
# 14 April 2014

def get_integer(n): # This function accepts a string, converts to integer and returns it
    integer = input("Enter " + n + ":\n")
    while not integer.isdigit ():
        integer = input("Enter " + n + ":\n")
    integer = eval(integer)
    return integer
        
def calc_factorial (n): # This function calculates the factorial of a value n
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
    
    
    
    
    
    