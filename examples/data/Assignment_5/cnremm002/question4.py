"""Graph
Emmanuel Conradie
17 april 2014"""

import math
#input
def main():
    function = input("Enter a function f(x):\n")
    x = 0
    y = 0
#graph
    for rows in range(10,-11,-1):
        for column in range(-10,11,1):
            x = column
            roundfx = round(eval(function))
#f(x)            
            if roundfx == rows:
                print("o", end="")
#axis            
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
main()