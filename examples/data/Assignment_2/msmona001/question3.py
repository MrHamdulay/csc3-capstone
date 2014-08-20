#Assignment 2
#Question 3
#Onalerona Mosimege

import math
area = 0
pi = 2
constant = math.sqrt(2)
x = 2/constant
while x != 1:
    pi = pi * x
    constant = math.sqrt(2 + constant)
    x = 2/ constant

print("Approximation of pi:", str(round(pi,3)))
radius = eval(input("Enter the radius:\n"))
area = ((radius)**2) * pi
print("Area:", str(round(area,3)))