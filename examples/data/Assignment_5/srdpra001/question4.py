"""
Prashanth Sridharan
SRDPRA001
Assignment 05
Question 04
"""

import math
from math import*
f= input("Enter a function f(x):\n")# input the function and the variable name is called f
f = f.replace("x", "y") #returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.
r = range(-10,11) #assigning a range to the loops
#The following are for creating the graph
for x in r: 
    for y in r:
        if -x==round(eval(f)):
            print("o", end="")
        elif x==0 and y ==0:
            print("+", end="")
        elif x==0:
            print("-", end="")
        elif y ==0:
            print("|", end="")
        else:
            print(" ",end="")
    print() #print the graph
            