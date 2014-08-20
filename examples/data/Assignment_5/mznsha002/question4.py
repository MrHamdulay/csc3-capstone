# 16 April 2014
# Shaun Muzenda
# Drawing a text based graph based on a user inputed function

import math

def main():
    function = input("Enter a function f(x):\n")        #asks the user for a given function
    x = 0                                               #initial vaule of x set to 0
    y = 0                                               #initial vaule of x set to 0

    for rows in range(10,-11,-1):                       #the range for the y-axis
        for column in range(-10,11,1):                  #the range for the x-axis
            x = column
            round_fx = round(eval(function))            #rounds the value of the given value
            if round_fx == rows:
                print("o", end="")                      #prints the plotted values as " o's "
            if rows == 0 and column == 0 and not rows == round_fx:
                print("+", end="")
            if column == 0 and not rows == 0 and not rows == round_fx:
                print("|", end="")                      #prints the y-axis using " |'s "
            if rows == 0 and not column == 0 and not rows == round_fx:
                print("-", end="")                      #prints the x-axis using " -'s "
            else:
                if not rows == 0:
                    if not column == 0:
                        if not rows == round_fx:
                            print(" ", end="")          #leaves the unplotted parts of the screen blank
        print()                                         #prints the graph
main()