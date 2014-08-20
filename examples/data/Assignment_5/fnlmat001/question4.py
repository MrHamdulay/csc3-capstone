"""program that draws a text-based graph of a mathematical function f(x)
Matthew Finlayson - FNLMAT001
15/04/2014"""

import math

function = input("Enter a function f(x):\n") 

for y in range (-10,11): # y takes on each value along the y axis
    for x in range (-10,11): # x takes on each value along the x axis
        
        y_coord = round(eval(function)) # gets the y coordinate for each point x 
        
        if (y_coord == -y): # if the coordinate is the current value of y along the y axis
            print("o", end = "")
        
        elif (x == 0 and y == 0): # identifies the origin
            print("+", end = "")        
        elif (x==0): # identifies the y axis
            print("|", end = "")
        elif (y==0): # identifies the x axis
            print("-", end = "")
        else: # all other space that is not part of the axis or the graph
            print(" ",end = "")
            
        
        
    print()