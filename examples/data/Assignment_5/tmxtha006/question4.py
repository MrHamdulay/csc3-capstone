"""the program draw a text-based graph of a mathematical function
Hebert Tema- TMXTHA006
15 April 2014"""

#get the equation of the graph
function=input("Enter a function f(x):\n")

import math

#print out a graph
for y in range(10,-11,-1):            #loop for the range
    for x in range(-10,11):           #loop for the domain  
        if y==round(eval(function)): print("o", end="")         #point of the graph on the grid
        elif x==0 and y==0: print("+", end="")         #the origin
        elif x==0: print("|", end="")                  #the y axis
        elif y==0: print("-", end="")                  #the x axis
        else: print(" ", end="")                       #unoccupied pixel
    print("")