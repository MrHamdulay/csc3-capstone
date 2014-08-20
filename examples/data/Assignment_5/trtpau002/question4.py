"""Mathematical function
Paul Truter
17 April 2014"""

import math

function = input("Enter a function f(x):\n")
y=0
x=0
    
for rows in range(10,-11,-1):
            for column in range(-10,11,1):
                        x=column
                        fx = round(eval(function))
                        if fx == rows:
                                    print("o", end="")
                        if rows == 0 and column == 0 and not rows == fx:
                                    print("+", end="")
                        if column == 0 and not rows == 0 and not rows == fx:
                                    print("|", end="")
                        if rows == 0 and not column == 0 and not rows == fx:
                                    print("-", end="")
                        else:
                                    if not rows == 0:
                                                if not column == 0:
                                                            if not rows == fx:
                                                                        print(" ", end="")
            print()        
