# Program to calculate pi and the area of a circle
# Nevarr Pillay - PLLNEV006
# 8 March 2014

import math

def pi():
    pi = 2
    count = 0
    newnum = 0
    while(newnum != 1):
        newnum = math.sqrt(2)
        for i in range(count):
            newnum = math.sqrt(2 + newnum)
        newnum = 2/newnum    
        pi *= newnum 
        count += 1
    return pi   

def area(radius):
    area = pi() * (radius**2)
    outarea = round(area,3)
    return outarea

def main():
    print("Approximation of pi:",round(pi(),3))
    radius = eval(input("Enter the radius:\n"))
    print("Area:", area(radius))
    
main()  

