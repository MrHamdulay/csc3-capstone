# Question 3 Assignment 2
# Author: Julius Stopforth STPJUL004
# Date: 10/03/2014

from math import sqrt

approx_pi = 2
x = 0
next_term = 2/(sqrt(2 + x))


while next_term != 1:
    approx_pi *= next_term
    x = sqrt(2 + x)
    next_term = 2/(sqrt(2 + x))
    
print("Approximation of pi:", round(approx_pi,3))
r = eval(input("Enter the radius:\n"))

#using unrounded pi
circ_area = round((approx_pi*(r**2)),3)

print('Area:', circ_area)