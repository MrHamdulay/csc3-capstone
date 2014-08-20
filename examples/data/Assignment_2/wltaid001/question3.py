#Aiden Walton
#WLTAID001
#Program to calculate area of circle given radius

import math

pi=2
den=math.sqrt(2)

while den<2:
    pi=pi*(2/den)
    den=math.sqrt(2+den)
    
print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
area=pi*r**2
print("Area:",round(area,3))
       
