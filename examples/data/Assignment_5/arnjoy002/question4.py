#Joy Arendse-Gorvalla
#ARNJOY002

import math #calls up math
def graph(): #new function
    func = input("Enter a function f(x):\n") #asks user for graph
    x = 0
    y = 0

    for rows in range(10,-11,-1): #loop - so that graph as an axis of -10&10
        for col in range(-10,11,1):
            x=col
            roundfx = round(eval(func))
            if roundfx == rows: #condition
                print("o", end="")
            if rows==0 and col==0 and not rows == roundfx:
                print("+", end="")
            if col == 0 and not rows == 0 and not rows == roundfx:
                print("|", end="")
            if rows==0 and not col==0 and not rows == roundfx:
                print("-", end="")
            else:
                if not rows == 0:
                    if not col == 0:
                        if not rows == roundfx:
                            print(" ", end="")
        print()
graph() #calls graph function