"""program to print mathematical functions (graphs) input by user
Mick Perring
17 April 2014"""

import math

function = input("Enter a function f(x):\n") # asks user to input a function
graph = ""   # sets 'graph' at nothing

for y in range (10, -11, -1): # y-axis range
    for x in range (-10, 11): # x-axis range
        if round(eval(function)) == y:
            graph += "o"        # adds 'o' to 'graph' if point lies on graph
        elif y == 0 and x != 0:
            graph += "-"        # adds x-axis ('-') to 'graph'
        elif y == 0 and x == 0:
            graph += "+"        # adds origin ('+') to 'graph'
        elif x == 0 and y != 0:
            graph += "|"        # adds y-axis ('|') to 'graph'
        else:
            graph += " "        # adds blank space to 'graph' if point not on graph or axis
    print (graph) # prints 'graph'
    graph = ""