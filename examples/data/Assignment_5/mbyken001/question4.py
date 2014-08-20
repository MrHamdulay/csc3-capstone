#graphing of  linear functions

import math

function=input("Enter a function f(x):\n")
x,y=0,0

for y in range (10,-11,-1):
    for x in range (-10,11,1):
        graph = round(eval(function))
        if x == 0 and y == 0 and y != graph:
            print("+",end="")
        elif y == graph:
            print("o",end="")
        elif y == 0:
            print("-",end="")
        elif x == 0:
            print("|",end="")
        else:
            print(" ",end="")
    print()
            
        
        