# text-based graph
# badugela mulisa
# 16 april 2014
import math
def graph():
    function = input("Enter a function f(x):\n")
    x = 0
    y = 0

    for y_values in range(10,-11,-1):
        for x_values in range(-10,11,1):
            x=x_values
            y=y_values
            r_function = round(eval(function)) # evaluating the function each time to compute the function value for different values of x.
            if r_function == y_values:
                print("o", end="")
            elif y_values==0 and x_values==0: # condition for origin
                print("+", end="")
            elif x_values ==0:  #condition that produes the y axis
                print("|", end="")
            elif y_values==0:
                print("-", end="") #condition that produces x axis
            else: # to print out the blank spaces of the graph
                if y_values != 0:
                    if x_values != 0:
                        if y_values != r_function:
                            print(" ", end="")
        print()
graph()