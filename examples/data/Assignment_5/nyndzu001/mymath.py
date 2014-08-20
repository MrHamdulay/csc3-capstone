"""Dzunisani Nyoni
17 April 2014
A program to calculate permutations"""

def get_integer (a):
    #Function to get the integer
    n= input ("Enter"+" "+a+":\n")
    while not n.isdigit ():
        n=input ("Enter"+" "+a+":\n")
    return int(n)

def calc_factorial (y):
    #A function to calculate the factorials.
    nfactorial=1
    for i in range (1, y+1):
        nfactorial *= i  
    return nfactorial
