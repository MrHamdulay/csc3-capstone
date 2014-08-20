"""Question 4 
Djavan Arrigone 17 April 2014"""

import math
#taking in user function
function = input("Enter a function f(x):\n")
#creating the grid
for y in range (10,-11,-1):
    for x in range (-10,11):
        #rounding values to ensure only integers will form part of plotted points
        graph = round(eval(function))
        #printing relevant values
        if y == graph:
                    print("o",end="")       
        elif x == 0 and y == 0:
            print("+", end="")
        elif y == 0:
            print("-", end="")
        elif x == 0:
            print("|", end="")
        else:
            print(" ", end="")
    print()
            
        
        