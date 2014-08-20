"""Drawing a graph
tayla george
17 april 2014"""

import math

def graph():
    function = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for rows in range(10,-11,-1): #axis
        for column in range(-10,11,1): #axis
            x = column
            roundfx = round(eval(function))
            if roundfx == rows:
                print("o", end="")
            if rows == 0 and column == 0 and not rows == roundfx:
                print("+", end="")
            if column == 0 and not rows == 0 and not rows == roundfx:
                print("|", end="")
            if rows == 0 and not column == 0 and not rows == roundfx:
                print("-", end="")
            else:
                if not rows == 0:
                    if not column == 0:
                        if not rows == roundfx:
                            print(" ", end="")
        print()
graph()