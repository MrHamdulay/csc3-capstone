#Code to draw any graph
#Saul Bloch
#14 April 2014

function = input("Enter a function f(x):\n")

import math #getting all math functions

def printAll():
    #y values range from -10 to 10
    for y in range(10,-11,-1):

        if y != 10:
            print("")
            
        #x values range from -10 to 10
        for x in range (-10,11):
            if round(eval(function)) == y: #if x coordinate = y coordinate...
                print("o", end = "")
            elif ((x==0) and (y==0)): #if at orgin
                    print("+",end = "")  
            elif y == 0: #if at x axis
                    print("-",end = "")
            elif x == 0: #if at y axis
                    print("|",end="")                  
            else: print(" ",end = "")
printAll()
              
            
    