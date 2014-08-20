"""Question 4 of Assignment 5: Function Plotting
Shaheel Kooverjee
17th April 2014"""

import math

funct = input("Enter a function f(x):\n")

for y in range(10,-11,-1): #through points on y-axis downwards
    for x in range(-10,11,1): #through points on x-axis rightwards
       
        xr = round(eval(funct)) #funtion value at x
        
        if xr == y: #function point
            print("o", end="")
        elif x == 0 and y == 0 and xr != y: #origin point
            print("+", end="")
        elif x == 0 and y != 0 and xr != y: #y-axis
            print("|", end="")
        elif x != 0 and y == 0 and xr != y: #x-axis
            print("-", end="")
        elif x != 0 and y != 0 and xr != y: #elsewhere in graph
            print(" ", end="")
            
    print()