# Assignment 5
# Functions to complete question3.py which calculates the no. of k-permutations of n items
# Frans van Hoek
# 14 April 2014

def get_integer(x):
    if x == 'k':
        while 0 < 1:
            integer = input("Enter k:\n")
            try:
                integer = int(integer)
            except ValueError:
                continue
            if 0 <= integer:
                return integer
                
                
    if x == 'n':
        while 0 < 1:
            integer = input("Enter n:\n")
            try:
                integer = int(integer)
            except ValueError:
                continue
            if 0 <= integer:
                return integer

def calc_factorial(x):
    import math
    fact = math.factorial(x)
    return fact