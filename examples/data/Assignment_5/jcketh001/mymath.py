#Program to calculate the number of k-permutations of n items
#Ethan Jackson
#16 April 2014

import math

def get_integer(n):
    hoog = ("Enter "+n+": \n")
    n = input(hoog)
    while not n.isdigit ():
        n = input(hoog)
    n = int(n)
    return n

def calc_factorial(n):
    nfactorial = 1
    for hos in range(1, n+1):#the range of the calculation
        nfactorial *= hos
    return nfactorial
    