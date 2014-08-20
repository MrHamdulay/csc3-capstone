"""placing a function on a graph
By Dylan
17 April 2014"""

import math


fx = input ( "Enter a function f(x):"'\n' )

for y in range (10,-11,-1):
        
        for x in range(-10,11):
                if round(eval(fx)) == y:
                        print("o", end='')    
                elif x == 0 and y == 0:
                        print("+", end='')
                elif y == 0:
                        print("-", end='')
                elif x == 0:
                        print("|", end='')
                else:
                        print(" ", end='')
        print()
        

    
