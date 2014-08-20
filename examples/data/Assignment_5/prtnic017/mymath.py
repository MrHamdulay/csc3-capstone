# Student Number: PRTNIC017
# Date: 4/13/14


def get_integer(message):
    n = input("Enter " + message + ":\n")
    while not n.isdigit():
        n = input("Enter " + message + ":\n")
    return eval(n)



def calc_factorial(value):
    factorial = 1
    for i in range(1, value + 1):
        factorial *= i
    return factorial