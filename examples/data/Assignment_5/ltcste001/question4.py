#stephanie Latchmanan(LTCSTE001)
#graphing a given function
#16 April 2014

import math

func=input("Enter a function f(x):\n")     #input a function

for y in range(10,-11, -1):
    for x in range(-10,11):
        yint=round(eval(func))             #creating values for y integers
        if yint == y:                      #point where graph exists
            print("o", end="")
        elif y==0 and x==0:                #create orgin point
            print("+", end="")
        elif y==0:
            print("-", end="")             #create x axis
        elif x==0:
            print("|",end="")              #create y axis
        else:
            print(" ", end="")
    print()