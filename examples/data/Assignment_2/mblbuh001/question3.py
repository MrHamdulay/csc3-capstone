# Program that calculates the value of PI and then computes and displays the area of a circle with radius entered by the user.
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 08 March 2014

from math import *

pi = 2
x = sqrt(2)
while (2/x)!=1:
    pi*=2/x
    x=sqrt(2+x)

print("Approximation of pi:", round(pi,3))
y=eval(input("Enter the radius:\n"))
z=eval("pi*y**2")
print("Area:", round(z,3))