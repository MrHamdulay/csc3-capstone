#Aaron Krishna 
#15 April 2014
#Draws the entered funtion on a graph

import math
function = input("Enter a function f(x):\n")

for y_value in range(10,-11,-1):
    for x_value in range(-10,11):
        x = x_value
        value = round(eval(function))
        if value == y_value:
            print("o", end="")
        elif y_value == 0 and x_value == 0:
            print("+", end = "")        
        elif y_value == 0:
            print("-", end = "")
        elif x_value == 0:
            print("|", end = "")
        else:
            print(" ", end = "")
    print("")