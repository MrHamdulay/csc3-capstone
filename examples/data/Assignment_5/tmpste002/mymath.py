""" Math module for Assignment 5 - Question 3 """
__author__ = 'Stephen Temple - TMPSTE002'
__date__ = '2014/04/13'


def get_integer(x):
    """ Input an integer and parse """
    n = input("Enter " + x + ":\n")
    while not n.isdigit ():
       n = input ("Enter " + x + ":\n")
    return eval(n)


def calc_factorial(x):
    """ x! mathematical function: x factorial """
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial