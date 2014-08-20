# A program that displays graphs
# Martin Batek
# 15 April 2014

import math
function = input("Enter a function f(x):\n")

for y in range(10,-11,-1):
    for x in range(-10,11):
        output = eval(function.replace("x","("+str(x)+")")) # There must be a bracket around the x so that all negative values of x in the function read as (-x)**n and not -x**n
        if round(output)==y:
            print("o",end="")
            # Curve
        else:
            if y==0 and x != 0:
                print("-",end="")
                # x-axis
            if x==0 and y!= 0:
                print("|",end="")
                # y-axis
            if y==0 and x==0:
                print("+",end="")
                # origin
            if x!=0 and y !=0:
                print(" ",end="")
                # spaces
    print() # Jumps to new line after printing for all x values of a y value
            