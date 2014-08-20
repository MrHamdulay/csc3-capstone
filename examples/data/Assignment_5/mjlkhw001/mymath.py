# My Math
# Khwezi Majola
# MJLKHW001
# 14 April 2014

def get_integer(x):
    j = x
    while not x.isdigit ():
        x = input ("Enter " + j + ":\n")
    x = eval (x)
    return x

def calc_factorial(y):
    j = 1
    for i in range (1, y+1):
        j *= i
    return j