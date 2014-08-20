#Liam Blignaut
#A program that calculates the value of pi and computes the area for the given area
#12/03/2014

import math
x=math.sqrt(2)
pi=2*(2/x)
while x!=2:
    x=math.sqrt(2+x)
    pi=pi*(2/x)
    b=round(pi,3)
print("Approximation of pi:",b)
radius=eval(input("Enter the radius:\n"))
w=round(pi*radius**2,3)
print("Area:",w)