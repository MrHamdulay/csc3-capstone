#Drawing graphs from functions
#Sohail Tulsi TLSSOH001
#15 April 2014


import math      # import math for functions
# create graph module 
def graph():
    function = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for rows in range(10,-11,-1):     # loop for rows of grid
        for colm in range(-10,11,1):     # loop for coloums of grid
            x=colm
            roundf = round(eval(function))
            if roundf == rows:
                print("o", end="")            # values of graph identified and print o
            if rows==0 and colm==0 and not rows == roundf:       # find centre
                print("+", end="")
            if colm == 0 and not rows == 0 and not rows == roundf:  # create y-axis
                print("|", end="")
            if rows==0 and not colm==0 and not rows == roundf:    # create x- axis
                print("-", end="")
            else:
                if not rows == 0:                       
                    if not colm == 0:
                        if not rows == roundf:
                            print(" ", end="")
        print()
graph()