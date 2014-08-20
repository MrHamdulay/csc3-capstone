#KRTDAK001

import math

def grapher():
    f = input("Enter a function f(x):\n")         #Function inputed by user
    y = 0
    x = 0
    
    
    for rows in range(10, -11, -1):                  #def rows and collumns
        for collumn in range(-10,11,1):
            x = collumn
            fx = round(eval(f))                       #eval the user input at each point
            if fx == rows:                           #The following "graph" each point and the axis
                print("o", end="")
            if rows == 0 and collumn == 0 and not rows == fx:
                print("+", end="")
            if collumn == 0 and not rows == 0 and not rows == fx:
                print("|", end="")
            if rows == 0 and not collumn == 0 and not rows == fx:
                print("-", end="")
            else:
                if not rows == 0:
                    if not collumn == 0:
                        if not rows == fx:
                            print(" ", end="")
        print()
grapher()