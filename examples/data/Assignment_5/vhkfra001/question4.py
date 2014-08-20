# Assignment 5
# Program to draw a function
# Frans van Hoek
# 14 April 2014

import math

import math
def main():
    function = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for y2 in range(10,-11,-1):
        for x2 in range(-10,11,1):
            x=x2
            roundfx = round(eval(function))
            if roundfx == y2:
                print("o", end="")
            if y2==0 and x2==0 and not y2 == roundfx:
                print("+", end="")
            if x2 == 0 and not y2 == 0 and not y2 == roundfx:
                print("|", end="")
            if y2==0 and not x2==0 and not y2 == roundfx:
                print("-", end="")
            else:
                if not y2 == 0:
                    if x2 != 0:
                        if y2 != roundfx:
                            print(" ", end="")
        print()
main()
