"""Program to Display the ASCII graph of a given function."""
#Liam Brodie
#April 2014
#BRDLIA004
#Assignment 5

import math

def FuncGraph():
    """Display's the graph of the given function"""
    Function = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for Rows in range(10,-11,-1):
        for Columns in range(-10,11,1):
            x=Columns
            RoundFx = round(eval(Function))
            if RoundFx == Rows:
                print("o", end="")
            if Rows==0 and Columns==0 and not Rows == RoundFx:
                print("+", end="")
            if Columns == 0 and not Rows == 0 and not Rows == RoundFx:
                print("|", end="")
            if Rows==0 and not Columns==0 and not Rows == RoundFx:
                print("-", end="")
            else:
                if not Rows == 0:
                    if not Columns == 0:
                        if not Rows == RoundFx:
                            print(" ", end="")
        print()
FuncGraph()