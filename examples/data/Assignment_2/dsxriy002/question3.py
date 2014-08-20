#Assignment 2
#Riya Desai
#8 March 2014

#let PI = the value of PI
#Let r = the radius
#Let area = the area of the circle

import math
x=2
PI = math.sqrt(2)
while (2/PI) != 1:
    x *= 2/PI
    PI = math.sqrt(2 + PI)

print("Approximation of pi:", round(x, 3)) 
r = eval(input("Enter the radius: \n"))


area = x*r**2

print("Area:", round(area, 3))