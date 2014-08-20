'''program to graph a function
ethan jackson
16 april'''

import math
#lets the user input a function
graph = input("Enter a function f(x):\n")
#plots a blank graph with the range 
for y in range (-10, 11):
        for x in range (-10, 11):
                if (-y == round(eval(graph))):
                        print ("o", end = "")
                elif (y == 0 and x == 0):
                        print ("+", end = "")
                elif (x == 0):
                        print ("|", end = "")
                elif (y == 0):
                        print ("-", end = "")
                else: 
                        print (" ", end = "")
        print ()
        #prints the graph
              
