#A3Q2
#Printing a triangle, given a height
import math
height = input("Enter the height of the triangle:\n")

if height.isdigit:
    height = eval(height) 
    for i in range(1,height+1):
        level = "*"*(i*2-1)  
        print("{0: ^{maxbase}}".format(level, maxbase= str(height*2-1)))