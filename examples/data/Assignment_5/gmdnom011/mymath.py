# Program to calculate factorials
# Nomsa Gamedze
# 14 April 2014

def get_integer(x):
    question = "Enter " + x + ":" + '\n'
    integer = input(question)
    while not integer.isdigit():
        integer = input(question)
    integer = eval(integer)
    return integer

def calc_factorial(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial