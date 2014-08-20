import math
def graph():
    function = input("Enter a function f(x):\n")
    x = 0
    y = 0
#defines the x and y axis and their range
    for x_axis in range(10,-11,-1):
        for y_axis in range(-10,11,1):
            x=y_axis
            roundfx = round(eval(function))
            #plots points where x=rounded y value 
            if roundfx == x_axis:
                print("o", end="")
            # defines the origin
            if x_axis==0 and y_axis==0 and not x_axis == roundfx:
                print("+", end="")
            #defines the y axis
            if y_axis == 0 and not x_axis == 0 and not x_axis == roundfx:
                print("|", end="")
            #defines the x axis
            if x_axis==0 and not y_axis==0 and not x_axis == roundfx:
                print("-", end="")
            else:
                #prints a space where x!=y
                if not x_axis == 0:
                    if not y_axis == 0:
                        if not x_axis == roundfx:
                            print(" ", end="")
        print()
graph()

