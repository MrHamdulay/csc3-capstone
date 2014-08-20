""" Function plotter
Keshin Vittee
16 April 2014"""

import math

fn = input("Enter a function f(x):\n")

# Domain is -10  to 10

for i in range(10,-11,-1):
    for x in range(-10,11,1):
        y = eval(fn)
        if round(y) == i:
            print("o",end="")
        elif x == 0 and i == 0:
            print("+",end="")
        elif x == 0:
            print("|",end="")
        elif i == 0:
            print("-",end="")
        else:
            print(" ",end="")
    print()
    
            