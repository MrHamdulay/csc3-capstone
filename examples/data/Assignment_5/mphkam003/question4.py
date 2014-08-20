"""a program to draw a text-based graph of a mathematical function f(x)
Kamogelo Mphela
15 April 2014"""
import math
# Define the function
function = input ("Enter a function f(x):\n")

for y in range(10,-11,-1): #range
    for x in range(-10,11): # domain
        real_function = round(eval(function))  # round off: for mainly trig functions
        if y == real_function:          # if y = f(x)
            print("o",end="")
        elif x==0 and y == 0 and y != real_function:
            print("+",end="")
        elif x==0 and  y != 0 and y != real_function:
            print("|",end="")
        elif y==0 and x!=0and y != real_function:
            print("-",end="")
        else:
            print(' ',end="")
    print()