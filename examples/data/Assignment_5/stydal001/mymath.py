# Dalise Steynfaard
# STYDAL001
# Assignment 5, question 3
# 12-04-2014

def get_integer(item):
    n = input ("Enter " + item +":\n")
    while not n.isdigit ():
        n = input ("Enter " + item +":\n")
    n = eval (n)
    return n

def calc_factorial(f):
    factorial = 1
    for i in range (1, f+1):
        factorial *= i    
    return factorial