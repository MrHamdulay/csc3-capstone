"""Get function and draw graphs of those functions
Khanyisile Morudu
14 April 2014"""

import math
function = input("Enter a function f(x):\n")

#drawing the graph 
for y in range(-10, 11):
    for x in range(-10,11):
        if round(eval(function)) == -y:
            print("o", end = "")
        else:
            if (x ==0) and (y ==0): # origin 
                print("+", end= "")
            else:
                if y ==0: # printing y axis lines
                    print("-", end = "")
                else: #print x axis lines
                    if x == 0:
                        print("|", end = "")
                    else:
                        print(" ", end = "")
    print()