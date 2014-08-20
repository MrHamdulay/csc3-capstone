#Assignment 5 Question 4 
#draw a text-based graph of a mathematical function f(x)
#WRTJOS001 Joshua Wort
#14 April 2014

import math

function=input("Enter a function f(x):\n")

for y in range(10,-11,-1):
    for x in range(-10,11):
        roundy=round(eval(function))
        if roundy==y:
            print("o",end="")
        elif y==0 and x==0:
            print("+",end="")
        elif y==0:
            print("-",end="")
        elif x==0:
            print("|",end="")
        else:
            print(" ",end="")
    print()
    