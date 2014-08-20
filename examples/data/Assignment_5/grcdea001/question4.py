"""Program to draw a ascii graph of a function of f : Prac 5 Question 4
Dean Gracey
4/15/2014"""

import math

function = (input("Enter a function f(x):\n"))



for y in range (-10,11):
    
    for x in range(-10,11):
        if (-y==round(eval(function))):
            print("o", end = "")
        elif (y==0) and (x==0):
            print("+",end="")
        
        elif (y == 0):
                print("-",end = "") 
        elif (x == 0):
                print("|",end = "")        
        else:
            print(" ",end = "")
    print("") 