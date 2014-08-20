#Tofunmi Olagoke
#15 April 2014
#OLGMOF001
#Program drawing a straight line graph

import math

def functiongraph():
    Thefunc = input("Enter a function f(x):\n") #inputted function
    x = 0
    y = 0

    for horizontal in range(10,-11,-1):
        for vertical in range(-10,11,1):
            x=vertical
            
            Usablefunc=round(eval(Thefunc)) 
            
            #y-axis
            if vertical == 0 and not horizontal == 0 and not horizontal==Usablefunc:
                print("|", end="")
            
            #x-axis
            elif horizontal==0 and not vertical==0 and not horizontal==Usablefunc:
                print("-", end="")
            
            #plotted points
            elif Usablefunc == horizontal:
                print("o", end="")
            
            #origin
            elif horizontal==0 and vertical==0 and not horizontal==Usablefunc:
                print("+", end="")
            
            #space
            else:
                if not horizontal == 0 and not vertical == 0 and not horizontal == Usablefunc:
                            print(" ", end="")                    
        print()
functiongraph()
 