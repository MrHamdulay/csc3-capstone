'''Assignment 5 question 3 myMath
Adam Smith
16 April 2014'''

def get_integer(variable):    #ensures the right variable is assigned to the right value
    value = input ("Enter " + variable + ":\n")
    while not value.isdigit ():
        value = input ("Enter " + variable + ":\n")
    value = eval (value)
    return value

def calc_factorial(value): #calculates the factorial by multiplying all numbers up to the number
    factorial = 1
    for i in range (1, value+1):
        factorial *= i
    return factorial
       
    