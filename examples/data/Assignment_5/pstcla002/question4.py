"""Graph Function
Claudia Pastellides
15 April 2014"""

import math

function=input("Enter a function f(x):\n")

for y in range(10,-11,-1): #range of function
    if y!=10:
        print("")
    
    for x in range(-10,11): #domain of function, within the range
        co_ord=eval(function) #f(x)
        roundco_ord=round(co_ord) #explicit points only roundco_ord is the y
        if x==0 and y==0 and roundco_ord !=0:#origin
            print("+",end="")        
        elif y==0 and roundco_ord!=0:#x axis
            print("-",end="")
        elif x==0 and roundco_ord!=y:#y axis
            print("|",end="")
        elif y==roundco_ord:
            print("o",end="")
        else:
            print(" ",end="")
            