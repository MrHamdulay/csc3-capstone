#Shahrain Coovadia
#CVDSHA002

import math
def plotter():
    func=input("Enter a function f(x):\n")          #input function
    x=0                  
    y=0
    
    for hor in range(10,-11,-1):                    #for x axis and x variable
        for vert in range(-10,11):                    #for y axis and y variable
            x=vert
            fx=round(eval(func))
            if fx==hor:
                print("o", end="")                         #plots points
            if hor==0 and vert==0 and hor!=fx:                 
                print("+", end="")                    #maps the orign
            if vert==0 and hor!=0 and hor!=fx:
                print("|", end="")                       #vertical axis
            if hor==0 and vert!=0 and hor!=fx:
                print("-", end="")                    #horizontal axis
            else:
                if hor!=0:
                    if vert!=0:
                        if hor!=fx:
                            print(" ", end="")             
        print()
plotter()