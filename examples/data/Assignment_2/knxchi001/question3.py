#Assignment 2
#Queston 3

import math 

PI= 2
denominator= math.sqrt(2)

while denominator <2:
    PI= PI * 2/denominator 
    denominator= math.sqrt(2+denominator)
    
print("Approximation of pi:", round(PI,3))

radius= eval(input("Enter the radius: \n"))

area= PI*radius**2
print("Area:", round(area, 3))

