# Question 4 - Assignment 5
# A program used to draw a graph
# Written by: Laene van Niekerk

import math

equation_1 = input("Enter a function f(x):\n")
for y in range(10, -11, -1):
        for x in range(-10, 11):
                y_real = eval(equation_1.replace("x", "("+str(x)+")"))  # Brackets to ensure all negative values of x reads as -x
                y_real = round(y_real)
                if y_real == y:
                        print("o", end="")             # Plots point of the graph
                else:
                        if y == 0 and x != 0:           # Prints x-axis
                                print("-", end="")
                        elif x == 0 and y != 0:         # Prints y-axis
                                print("|", end="")
                        elif y == 0 and x == 0:         # Prints origin
                                print("+", end="")
                        elif x != 0 and y != 0:         # Prints empty space between values
                                print(" ", end="")
                
        print()