#Program to find area of circle using pi
#Paul Truter
#14 March 2014

import math

pi=round(math.pi,3)
print("Approximation of pi:",pi)
r=eval(input("Enter the radius:\n"))
Area=pi*(r**2)
print("Area:",round(Area,3))