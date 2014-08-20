"""Draws a text-based graph of a mathematical function f(x)
Ricky Conn
CNNRIC004
15/04/2014"""
import math

#def convertStrFuncToValue(function):
    #stringWithSubX = ""
    #value=0
    #for x in range(-10,11):
            #value = eval(function)
            
            
        
        
    

function = input("Enter a function f(x):\n")

#prints axes
for y in range(10,-11,-1):
    for x in range(-10,11):
        value = round(eval(function))
        #if((value >= y)and(value < y+1)):
        if(y==value):
            print("o",end="")
        elif((x == 0) and (y != 0)):
            print("|",end="")
        elif((x != 0) and (y != 0)):
            print(" ",end="")
        elif((y == 0) and (x != 0)):
            print("-",end="")
        elif((x==0)and(y==0)):
            print("+",end="")
    print()
    
#convertStrFuncToValue(function)