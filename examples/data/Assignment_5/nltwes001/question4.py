#ASSIGNMENT 5
#QUESTION 4
#NLTWES001

import math

function=input("Enter a function f(x):\n")
    
#Draw graph
for y in range(-10,11):
    for x in range(-10,11):
        xcord=x
        ycord=-y
        if ycord==round(eval(function)):
            print("o",end="")
        elif xcord==0 and ycord==0:
            print("+",end="")
        elif xcord==0:
            print("|",end="")
        elif ycord==0:
            print("-",end="")
        else:
            print(" ",end="")
    print()
    
        