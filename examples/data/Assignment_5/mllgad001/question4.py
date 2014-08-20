# program to draw a text based graph of a mathematical function
# Gadija Moollagie
# 17 April 2014

import math

def main():
    function = input("Enter a function f(x):\n") # prompts user to enter function
    x = 0
    
    for y_rows in range(10,-11,-1):
        for x_col in range(-10,11,1): # nested loops to scan through area of graph
            x = x_col 
            func = round(eval(function)) # rounds function and gets y value
            if func == y_rows: # where rounded value = y value in the rows, prints 'o' to draw graph
                print("o", end="")
            if y_rows == 0 and x_col == 0 and not y_rows == func:
                print("+", end="") # plots origin where the x and y axes are 0 and does not equal y value
            if x_col == 0 and not y_rows == 0 and not y_rows == func:
                print("|", end="") # plots y axis as long as its not equal to function 
            if y_rows==0 and not x_col==0 and not y_rows == func: # plots x axis as long as its not equal to function
                print("-", end="")
            else: # where the graph and axes does not occur, print empty space
                if not y_rows == 0:
                    if not x_col == 0:
                        if not y_rows == func:
                            print(" ", end="")
        print()
main()
