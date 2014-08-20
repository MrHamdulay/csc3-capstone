"""Muhammad Ahmad
AHMMUH009
17 April 2014"""

import math         #Makes use of the math library
def plotter():
    func = input("Enter a function f(x):\n")        #asks user for the function
    x = 0
    y = 0

    for rows in range(10,-11,-1):           #range of x-axis
        for col in range(-10,11,1):         #range of y-axis
           
            x=col
            fx = round(eval(func))          #makes function python-readable (evaluates it)
            if fx == rows:
                print("o", end="")          #graphs the funtion onto the graph
            if rows==0 and col==0 and not rows == fx:       #graphs the origin
                print("+", end="")
            if col == 0 and rows != 0 and rows != fx:           #prints the x-axis
                print("|", end="")
            if rows==0 and col!=0 and rows != fx:               #prints the y-axis
                print("-", end="")
            else:
                if  rows != 0:
                    if col != 0:
                        if rows != fx:
                            print(" ", end="")
        print()
plotter()

