#Permutations
#Devaksha Pillay
#15 April 2014

import math

#get input from user - ensure it is a digit
def get_integer(x):
    if x == "n":
        x = input ("Enter n:\n")
        while not x.isdigit():
            x = input("Enter n:\n")
        x = eval(x)
        return x
    if x == "k":
        x = input ("Enter k:\n")
        while not x.isdigit():
            x = input("Enter k:\n")
        x = eval(x)
        return x        
        
def calc_factorial (x):
    x = (math.factorial(x))
    return x
    