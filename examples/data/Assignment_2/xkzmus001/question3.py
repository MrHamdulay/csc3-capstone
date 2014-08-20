#question3.py
#Author : Musa Xakaza
#Date : 07/03/2014

import math

sqrt1 = math.sqrt(2)
sqrt2 = math.sqrt(2 + sqrt1)
sqrt3 = math.sqrt(2 + sqrt2)

p = 2 * (2/sqrt1) * (2/sqrt2) * (2/sqrt3)
print("Approximation of pi:",round(p,3))
radius = eval(input("Enter the radius:\n"))
area = p * radius**2
print("Area:",round(area,3))