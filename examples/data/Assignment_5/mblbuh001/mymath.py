# question1.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 15 April 2014

def get_integer(value):
    value1 = input ("Enter "+value+":\n")
    while not value1.isdigit ():
        value1 = input ("Enter "+value+":\n")
    value = eval (value1)
    return value

def calc_factorial(value):
    factorial = 1
    for i in range (1, value+1):
        factorial *= i
    return factorial