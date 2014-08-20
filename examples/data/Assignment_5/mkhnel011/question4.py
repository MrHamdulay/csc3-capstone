""" a program that draws a text-base graph of f(x)
nelisile mkhwebane
16/04/2014"""

import math

def graph():
    
    function = input("Enter a function f(x):\n") # get the function from user
    
    for y in range (10,-11,-1):
        for x in range(-10,11):
            funct= round(eval(function))
            if funct == y:
                print ("o", end="") 
            elif x==0 and y==0 :
                print("+",end="")            
            elif x==0:
                print("|",end="")
            elif y==0:
                print("-",end="")
            else:
                print(" ",end="")
        print()
graph()
        