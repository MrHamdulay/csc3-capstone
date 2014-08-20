#drawing functions
#anna borysova
#2014-04-15

import math

function = input("Enter a function f(x):\n")

def f(x):
    y = round(eval(function))
    return y

for i in range(10,-11,-1):
    for j in range(-10,11,1):
        if i == f(j):
            print("o", end="")
        elif i == 0 and j == 0:
            print("+", end="")
        elif i == 0:
            print("-", end="")
        elif j == 0:
            print("|", end="")
        
        else:
            print(" ", end="")
    print()
    