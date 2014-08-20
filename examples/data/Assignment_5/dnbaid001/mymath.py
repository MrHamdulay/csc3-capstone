#Assignment 5 - Question 3
#Aidan de Nobrega
#13/04/2014

def get_integer(number):
    '''returns digit string as number'''
    x = input ("Enter " + number + ":\n")
    while not x.isdigit ():
        x = input ("Enter " + number + ":\n")
    x = eval (x)
    return x

def calc_factorial(num):
    '''calculates factorial of a number'''
    factorial = 1
    for i in range (1, num+1):
        factorial *= i
    return factorial
