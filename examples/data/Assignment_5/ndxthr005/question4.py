"""question3: program to draw given graph 
thrianka naidoo
ndxthr005"""

import math

function = input("Enter a function f(x):\n")        #input from user

for y in range(10,-11,-1):                          #loops to create the grid
    for x in range(-10,11):
        fx=eval(function)                           #change string to float
        
        if (y == round(fx)):                        #print function
            print("o",end="")

        elif (x==0) and (y ==0):                    #At point 0, print centre --- +
            print("+",end="")
 
        elif (x==0):                                #y-axis
            print("|",end="")

        elif (y==0):                                #x-axis
            print("-",end="")

        else:                                       #grid
            print(" ",end="")
    print()