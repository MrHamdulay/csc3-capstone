"""a program to draw a text-based graph of a mathematical function f(x)
Author: Barnett msiska
Date: 15/04/2014"""
import math
function = input("Enter a function f(x):\n")
for y in range(10, -11, -1):
    for x in range(-10, 11):
        value = round(eval(function))
        equation = "y==" + str(value)
        if (round(eval(equation))):
            print("o", end="")        
        elif x==y and x==0:
            print("+", end="")
        elif x==0:
            print("|", end="")
        elif y==0:
            print("-", end="")
        else:
            print(" ", end="")
    print()