"""CSC1015F Assignment 5 Question 4
Xola Matlanyane MTLXOL002
17 April 2014"""

import math #in order to use existing mathematical functions

def graph():
    fx = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for r in range(10,-11,-1):      #for the rows
        for c in range(-10,11,1):       #for the columns
            x=c
            roundfx = round(eval(fx))
            if roundfx == r:        #plotting the graph
                print("o", end="")
            if r==0 and c==0 and not r == roundfx:
                print("+", end="")      #creates the "origin"
            if c == 0 and not r == 0 and not r == roundfx:
                print("|", end="")      #creates the y-axis
            if r==0 and not c==0 and not r == roundfx:
                print("-", end="")     #creates the x-axis
            else:
                if not r == 0:
                    if not c == 0:
                        if not r== roundfx:
                            print(" ", end="") #the "filler" of the grid
        print()
graph()