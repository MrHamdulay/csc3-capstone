#Asil Motala
#13 April 2014
#Assignment 5
#Question 3

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