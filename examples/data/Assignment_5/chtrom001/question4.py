# program to draw functions on y-x axis
#romelon chetty( chtrom001)
#question 4


import math 
def graph():
    function = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for rows in range(10,-11,-1):   
        for col in range(-10,11,1):  #set ranges to axis limits
            x=col
            roundfx = round(eval(function))
            if roundfx == rows:
                print("o", end="")
            if col == 0 and not rows == 0 and not rows == roundfx:
                print("|", end="")
            if rows==0 and not col==0 and not rows == roundfx:
                print("-", end="")
            if rows==0 and col==0 and not rows == roundfx:
                                print("+", end="")      
            else:
                if not rows == 0:
                    if not col == 0:
                        if not rows == roundfx:
                            print(" ", end="")
        print()
graph()

