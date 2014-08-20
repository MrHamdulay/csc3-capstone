"""a program to print a graph 
   kevin kumasamba
   16 april 2104"""
import math

# the user needs to enter a function which will be x plus something
# the x has to have a value because a function is y=f(x) so,
x=0
function = input("Enter a function f(x):\n") 

for frange in range(10,-11,-1): 
    for fdomain in range(-10,11,1):
        # if i wanted to print a box of this domain and range: print("X", end="")
    # print()
        # the function must look for the point where the x value of the function is equal to something (round it off to make life easier) so,
        # x can be any point on the domoain so,
        x=fdomain
        # now that we have x, y=f(x) makes sense and can print for each value in the domain so,
        rf=round(eval(function))
# to make a graph, there needs to be points, axes, and an origin

# this condition needs to be satisfied in order for a point to be shown on the graph        

        if rf==frange:
            print("o", end="")

# this condition is for the origin, y and x are equal at 0         

        if frange==fdomain and frange==0 and fdomain==0 and not rf==frange:
            print("+", end="")

# this condition prints the x axis

        if not rf==frange and fdomain==0 and not frange==0:
            print("|", end="")
        
# this condition prints the y axis

        if not rf==frange and not fdomain==0 and frange==0:
            print("-", end="")
        
# the graph also needs spaces to fill up the box
# the conditions need to be one function
# for there to be empty boxes: y is not equal to anything, the x axis is not equal to anything, and the y axis is not equal to anything
        else:
            if not frange==0:
                if not fdomain==0:
                    if not rf==frange:
                        print(" ", end="")
    print()
        
