"""
calculating the number of k-permutations of n items
Nosipho Khumalo
11 April 2014
"""

def get_integer(n):
    integer = input ("Enter " +  n + ": \n")
    while not integer.isdigit ():
        integer = input ("Enter " +  n + ": \n")
    return eval(integer)

def calc_factorial(n):
    factorial = 1
    for i in range (1, n+1):
        factorial *= i 
    return factorial