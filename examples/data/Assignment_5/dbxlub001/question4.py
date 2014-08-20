

import math
def Mr_Plotter():
    #call function
    function = input("Enter a function f(x):\n")
    
    #draw graph seet
    for y_values in range(10,-11,-1):
        for x_values in range(-10,11,1):
            #define x for the function
            x=x_values
            #round f(x) values
            round_Function = round(eval(function))
            #draw origin
            if y_values==0 and x_values==0 and y_values != round_Function:
                print("+", end="")
                #draw axis
            if x_values == 0 and y_values != 0 and y_values != round_Function:
                print("|", end="")
            if y_values==0 and x_values !=0 and y_values != round_Function:
                print("-", end="")
                #plot graph
            if round_Function == y_values:
                print("o", end="")

            #leave blanks where there is no graph

            else:
                if y_values != 0:
                    if x_values != 0:
                        if y_values != round_Function:
                            print(" ", end="")
        print()
Mr_Plotter()