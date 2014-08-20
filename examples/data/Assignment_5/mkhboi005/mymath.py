""" question1.py
 Name: Tumi Mkhawana
 Student Number: MKHBOI005
Date: 15 April 2014"""
#obtain an integer value
def get_integer(value):
    value1 = input ("Enter "+value+":\n")
    while not value1.isdigit ():
        value1 = input ("Enter "+value+":\n")
    value = eval (value1)
    #save the integer
    return value
#obtain the factorial
def calc_factorial(value):
    factorial = 1
    for i in range (1, value+1):
        factorial *= i
    #save the factorial
    return factorial