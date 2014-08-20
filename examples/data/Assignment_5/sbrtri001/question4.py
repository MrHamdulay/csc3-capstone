'''Assignment 5, question 4
Tristan Subroyen
14 April 2014'''

import math # imports math module

def plotGraph():
    y = 0 # initializes x for input
    x = 0 # initializes y for input
    eq = input("Enter a function f(x):\n") # asks user for input
    
    # Loop for y-axis
    for i in range (10,-11,-1):
        # Loop for x-axis
        for j in range (-10,11,1):
            x = j # assigns input 'x' to j value
            newEq = round(eval(eq)) # rounds evaluated input function so that it can be compared...
            if newEq == i: # if the function is defined at a point on the graph...
                print("o", end="")
            if i == 0 and j == 0 and i != newEq: # if at the origin...
                print("+", end = "")
            if j == 0 and i != 0 and i != newEq: # if on the y-axis...
                print("|", end="")
            if i==0 and j != 0 and i != newEq: # if on the x-axis...
                print("-", end="")
            else: # For all points not at above points
                if i != 0:
                    if j != 0:
                        if i != newEq:
                            print(" ", end= "")
        print('')
                        
if __name__ == '__main__':
    plotGraph()
                
        
    