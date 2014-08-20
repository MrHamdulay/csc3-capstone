# Finding the area of a circle
# Andrew Forson
# FRSAND012

import math
x = 2
y = math.sqrt(2)

while y < 2:
    x = x*2/y
    y = math.sqrt(2+y)
    
print("Approximation of pi:" , round(x,3))
b = eval(input("Enter the radius: \n"))
z = x*b**2
print("Area:" ,round(z,3))






