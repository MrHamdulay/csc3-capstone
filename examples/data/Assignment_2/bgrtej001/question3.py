#Assignment 2, Question 3
#Tejasvin Bagirathi BGRTEJ001
#11/03/2014

import math
x=2
g = 0
while g != 1:
    g = math.sqrt(2 + g) #Original Formula
    x = x*(2/g) #2/(2/math.sqrt(2+g)
    if (2/g) == 1: break #When 2/g = 1, quit loop
    
print("Approximation of pi:", round(x,3))
radius = eval(input("Enter the radius:\n"))
area = x*radius*radius
print("Area:", round(area, 3))

 
