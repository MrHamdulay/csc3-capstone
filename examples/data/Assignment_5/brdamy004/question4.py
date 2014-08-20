# Assignment 5 question 4
# Amy Brodie
# 16/04/2014

import math

function = input("Enter a function f(x):\n")
graph = ""

# checking all positions in the graph between -10 and 10
for y in range(10,-11,-1):
    for x in range(-10,11):
        if not (-10 <= eval(function) <= 10) :
            if x == 0:
                graph += "|"
            elif y == 0:
                graph += "-"
            elif (-10<=x<=10):
                graph += " "            
            continue
        elif round(eval(function)) == y:
            graph += "o"
        elif (x==0) and (y==0):
            graph += "+"
        elif x == 0:
            graph += "|"
        elif y == 0:
            graph += "-"
        else:
            graph += " "
    graph += "\n"
    
print(graph)
        
            