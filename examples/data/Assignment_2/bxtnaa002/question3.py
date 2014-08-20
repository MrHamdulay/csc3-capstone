# question3.py
# a program that calculates the value of PI and then computes and displays the area of a circle with radius entered by the user
# author: bxtnaa002

import math

n = math.sqrt(2)
pi = 2*(2/n)
while n!= 2: # denominator n has to equal to 2 for the size of the term to be 1.
    n = math.sqrt(2+n)
    pi = (pi*(2/n))
    
print("Approximation of pi:",round(pi, 3))
radius = eval(input("Enter the radius:\n"))
print("Area:",round((pi*(radius**2)),3))
