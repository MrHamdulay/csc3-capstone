#Drawing Graphs
#Devaksha Pillay
#15 April 2014

import math
graph = input("Enter a function f(x):\n")
x,y = 0,0

for y in range(10,-11,-1): 
    for x in range(-10,11,1):
        graph2 = eval(graph)
        graph3 = round(graph2)
        if y == graph3:
            print("o", end="")
        if y==0 and x==0 and y != graph3:
            print("+", end="")
        if x == 0 and y != 0 and y != graph3:
            print("|", end="")
        if y==0 and x!=0 and y != graph3:
            print("-", end="")
        else:
            if y != 0 and x !=0 and y!= graph3:
                print(" ", end="")
    print()