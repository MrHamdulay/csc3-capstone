# coding=utf-8


def get_integer(var):
    no = input("Enter " + var + ":\n")
    while not no.isdigit():
        no = input("Enter " + var + ":\n")
    return eval(no)


def calc_factorial(no):
    factorial = 1
    for i in range(1, no + 1):
        factorial *= i
    return factorial