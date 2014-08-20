# Assignment 2
# Question3
# Barry Su
# SXXBAR001
# 13 March 2014

import math

x = 2
y = math.sqrt(2)

while y < 2:
    x = x*2/y
    y = math.sqrt(2 + y)
    
print("Approximation of pi:",round(x,3))
r = eval(input("Enter the radius:\n"))
area = x*r**2
print("Area:",round(area, 3))
