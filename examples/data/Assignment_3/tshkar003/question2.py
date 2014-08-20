#Assignment 3 question 2
# Program for printing a triangle, given its height.
#By Karidas

import math
beat = input("Enter the height of the triangle:\n")

if beat.isdigit:
    beat = eval(beat) 
    for i in range(1,beat+1):
        level = "*"*(i*2-1)  
        print("{0: ^{maxbase}}".format(level, maxbase= str(beat*2-1)))