# program to draw a text-based graph of a mathematical function f(x).
# joshua gullan
# 16 April 2014

import math
function = input("Enter a function f(x):\n")
for y in range (10,-11,-1):
    for x in range (-10, 11):
        if y == round(eval(function)):
            print("o", end="")        
        elif x==0 and y==0:
            print ("+",end="")
        elif x == 0:
            print ("|",end="")
        elif y == 0:
            print ("-",end="") 
        else:
            print (" ",end="")
    print()