#Tashfia Amin #AMNTAS003 #Due:17 April 2014

import math

#create a variable for the function
function=input("Enter a function f(x): \n")

#create the axes for the graph
#insert the function into the graph
for y in range(10, -11, -1):                #graph starts at top and moves downwards in Python
    for x in range(-10, 11):                
        graph=round(eval(function))         #round because only using whole numbers
        if graph==y:
            print("o", end="")              #printing actual function
        elif graph!=y and x!=0 and y!=0:    
            print(" ",end="")               #printing empty spaces where no graph or axes
        elif graph!=y and x==0 and y==0:
            print("+",end="")               #printing (0,0) - intersection of x and y axes
        elif graph!=y and x==0:
            print("|",end="")               #printing y-axis
        elif graph!=y and y==0:
            print("-",end="")               #printing x-axis
    print()