"""mymath.py
Author: SWNREI001
a more usable version of the permutation program"""

def get_integer(s):
    n = input ("Enter " + s + ":\n")
    while not n.isdigit ():
        n = input ("Enter " + s + ":\n")
    return eval (n)

def calc_factorial(x):
    factorial = 1
    for i in range (1, x+1):
        factorial *= i
    return factorial