#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014/04/16
#Function       : To print a text based graph of a mathematical function
#Title          : Question 4


import math
from math import *
#Get function from the user
function = input("Enter a function f(x):\n")
for y in range(10,-11,-1):  #y values of the grid
    for x in range(-10,11):  # x values of the grid
        
        if y-0.5 < eval(function) < y+0.5:
            #Prints the function if it falls in a specific range
            print("o",end="")
        elif x == 0 and y!= 0:
            print("|",end="")
        elif x == 0 and y ==0:
            print ("+",end="")
        elif y == 0:
            print("-",end="")
        else:
            print(" ",end="")
    print()