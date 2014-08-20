'''Program to draw a text based graph f(X)
HAMZA EBRAHIM
17/04/14'''

# import math module for use below

import math

def main():
    # prompt user for function
    fnc = input("Enter a function f(x):\n")
    x = 0
    y = 0
    
    # making graph axis - defining graph range between [-10 & 10]
    for rows in range(10,-11,-1):
        for col in range(-10,11,1):
            
            x=col
            fx = round(eval(fnc))
            
            # prints actual function
            if fx == rows:
                print("o", end="")
                
            # prints origin of graph    
            if rows==0 and col==0 and not rows == fx:
                print("+", end="")

            # prints y-axis of graph
            if col == 0 and not rows == 0 and not rows == fx:
                print("|", end="")
            
            # prints x-axis of graph
            if rows==0 and not col==0 and not rows == fx:
                print("-", end="")

            else:
            # assists in plotting graph
                
                if not rows == 0:

                    if not col == 0:

                        if not rows == fx:

                            print(" ", end="")
        print()

# program ends

main()