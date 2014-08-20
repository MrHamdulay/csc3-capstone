#DJG
#Ass4 Q4
#16.04.14

import math

function = input("Enter a function f(x):\n")

 
y_increment = 4.9/10

for y in range(10,-11,-1):
    
    for x in range(-10,11):
        
        if (y-y_increment) <= eval(function) <= (y+y_increment):
                print("o", end="")
            
            
        else:   
            if x==0 and y==0:
                print("+", end="")
            
            elif y==0:
                print("-", end="")
                
            elif x==0:
                print("|", end="")
                
            else:
                print(" ", end="")
    print()
        
        