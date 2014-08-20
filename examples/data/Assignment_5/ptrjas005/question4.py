'''Jason Pietersen'''
#Program plotting a function

import math

function = input("Enter a function f(x):\n")
    
for y in range(10,-11,-1):
    for x in range(-10,11,1):
        
        if y == (round(eval(function))):
            point = "o"  
                    
        elif x == 0:
            point = "|"
            if y == 0:
                point = "+"
    
        elif y == 0:
            point = "-"
            
        else:
            point = " "
        
        print(point,end="")
            
    print()