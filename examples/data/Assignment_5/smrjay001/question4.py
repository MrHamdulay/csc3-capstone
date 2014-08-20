"""
Assignment 5 - Question 4
Fuction plotter using ASCII
Jayan Smart
SMRJAY001
April 2014
"""
import math

func = input("Enter a function f(x):\n")

for y in range(10, -11, -1):
    for x in range(-10, 11):
        f = func.replace("x", "("+str(x)+")")
        f=eval(f)
        f=round(f)
        if y==f:
            print("o", end="")
        elif x==0 and y==0:
            print('+', end="")
        elif x==0:
            print('|', end="")
        elif y==0:
            print("-", end="")
        else:
            print(' ', end="")
    print('')

