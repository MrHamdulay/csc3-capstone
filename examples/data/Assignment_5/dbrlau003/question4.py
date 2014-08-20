#Program to draw functions
#Lauren de Bruyn
#14 April 2014

import math
#Ask user to enter a function
function=input("Enter a function f(x): \n")
#draw grid
for y in range (-10,11):
    #plot graph on grid    
    for x in range (-10,11):
        newy=-y        
        if newy-0.5<=eval(function)<= newy+0.5:
            print("o",end='')
        elif x==0 and newy==0:
            print("+",end='')
        elif x==0 and newy!=0:
            print("|",end='')
        elif x!=0 and newy==0:
            print("-", end='')
        else:
            print(" ",end='')
    print("")
    
    
