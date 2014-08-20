# Dalise Steynfaard
# STYDAL001
# Assignment 5, question 4 - Drawing graphs of mathematical functions
# 13-04-2014

import math

def drawFunction():
    """Displays an inputted function as text on an axis of 10 to -10"""
    
    func = input("Enter a function f(x):\n")

    for y in range(10,-11,-1):
        if y!=10:
            print()
        for x in range(-10,11):
            if round(eval(func)) == y:
                print ("o", end="")            
            elif x==0 and y==0:
                print("+", end="")
            elif x == 0:
                print("|", end="")
            elif y == 0:
                print("-", end="")
            else:
                print(" ", end="")

drawFunction()