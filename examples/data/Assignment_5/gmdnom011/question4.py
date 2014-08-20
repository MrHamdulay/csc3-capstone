# Program to draw a text-based graph of a mathematical function
# Nomsa Gamedze
# 14 April 2014

import math

def draw():
    f = input("Enter a function f(x):"'\n')
    for y in range(-10, 11):
        y *= -1
        for x in range(-10,11):
            y_co_ord = round(eval(f.replace("x", "(" + str(x) + ")")))
            if y_co_ord == y:
                print("o", end="")
            elif x == 0 and y == 0:
                print("+", end="")
            elif x == 0:
                print("|", end="")
            elif y == 0:
                print("-", end="")
            else:
                print(" ", end="")
        print()

draw()