#A program to plot a graph of a given function, as inputted by the user
# Author: Emiel Zyde 
# Date: 17 April 2014

import math

def graph_plot():
    function = input("Enter a function f(x):\n")   
    
    for y in range (10, -11, -1):
        for x in range (-10, 11,1):
            x_rounded = round(eval(function))  #this allows us to substitute a function value into the formula and compare it to the y-value of the function at that point 
            if x_rounded == y:
                print("o", end ="")
            if x == 0 and y == 0 and not x_rounded == y:   
                print("+", end ="")
            if x == 0 and not y == 0 and not x_rounded == y:
                print("|", end ="")
            if y == 0 and not x == 0 and not x_rounded == y:
                print("-", end ="")
            elif not x == 0 and not y == 0 and not x_rounded == y:
                print(" ", end ="")     
        print()

graph_plot()