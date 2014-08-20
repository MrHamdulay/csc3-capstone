"""A programme to draw a text-based graph of any mathematical function
by Jeremy Smith SMTJER002
15 April 2014"""

import math

#receive an mathematical fucntion as an input
function = input("Enter a function f(x):\n")

#print a 10 x 10 graph of the input function
for a in range(-10, 11):
    for b in range(-10, 11):
        y = -a
        x = b
        z = x
        z = eval(function)
        z = round(z)
        if y == z:
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