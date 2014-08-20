#14/04/14
#Kureshlen Moodley
#MDLKUR001

import math 
#rounds numbers

graph=input("Enter a function f(x): \n")
 
for y in range (10, -11, -1):
    for x in range (-10, 11, 1):
        coordinate=round(eval(graph))
        if coordinate==y:
            print("o", end="")
#Entered Value        
        else:
            
            if y==0 and x==0: 
                print("+", end="")
            elif x==0: 
                print("|", end="")
            elif y==0:
                print("-", end="")
            else:
                print(" ", end="")
    print()
        