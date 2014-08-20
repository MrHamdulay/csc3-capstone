"""a program to print a linear function
   nitisha makanjee
   16 april 2014"""
import math

# the user needs to enter a function which will be x plus a constant
x=0
function = input("Enter a function f(x):\n")

for frange in range(10,-11,-1): 
    for fdomain in range(-10,11,1):
        # if i wanted to print a box of this domain and range: print("X", end="")
    # print()
        x=fdomain
        # now that we have x, y=f(x) makes sense and can print for each value in the domain so,
        rf=round(eval(function))
# to make a graph, there needs to be points, axes, and an origin

        if rf==frange:
            print("o", end="")

        if frange==fdomain and frange==0 and fdomain==0 and not rf==frange:
            print("+", end="")


        if not rf==frange and fdomain==0 and not frange==0:
            print("|", end="")
        

        if not rf==frange and not fdomain==0 and frange==0:
            print("-", end="")
        
# the graph also needs spaces to fill up the box
        else:
            if not frange==0:
                if not fdomain==0:
                    if not rf==frange:
                        print(" ", end="")
    print()
