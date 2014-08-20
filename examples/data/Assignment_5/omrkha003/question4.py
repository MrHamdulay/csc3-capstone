# program to draw a text-based graph of a mathematical function f(x)
# khadeejah omar
# 16 april 2014

import math

function = input("Enter a function f(x): \n")
x = 0

# scan area 
for i in range(10, -11, -1) : # y-values
    for j in range(-10, 11) : # x-values
        
        x = j
        f = round(eval(function)) # mathematical function, ie. f(x)
        
        if f == i : 
            print("o", end="") # prints graph
        if i == 0 and j == 0 and i != f :
            print("+", end="") # prints origin
        if j == 0 and i != 0 and i != f :
            print("|", end="") # prints y-axis
        if i == 0 and j != 0 and i != f :
            print("-", end="") # prints x-axis
        else: # area where graph and axis is not printed
            if i != 0 :
                if j != 0 :
                    if i != f :
                        print(" ", end="") # print empty space
    print()