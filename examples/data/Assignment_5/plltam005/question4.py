"""Drawing a graph
Tameryn Pillay
16 April 2014"""

import math

def graph():
    
    """Plotting the graph from the equation given"""
    
    function = input("Enter a function f(x):\n")
    
    for y_axis in range(10,-11,-1):
        for i in range (-10,11):
            x = i
            y = round(eval(function))
            if (y - math.floor(y)) >= 0.25:
                y= math.ceil(y)
            else:
                y = math.floor(y)
            if y_axis == y:
                print('o',end="")
            elif y_axis == i == 0 and y!=0:
                print("+",end="")
            elif y_axis == 0 and y!=0:
                print("-",end="")
            elif i == 0:
                print("|",end="")
            else:
                print(" ",end="")
        print()
            
graph()