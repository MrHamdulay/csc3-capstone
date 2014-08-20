from math import *
 
pi = 2
denom = sqrt(2)
 
while denom !=2:
 
 pi = pi * 2/denom
 
 denom = sqrt(2+denom)
 
print("Approximation of pi:",round(pi,3))
x=eval(input("Enter the radius: \n"))
radius=x*pi*x
print("Area:",round(radius,3))