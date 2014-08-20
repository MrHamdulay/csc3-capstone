#Program to calculate the approximate value of Pi and calculate the area of a circle from a given radius
#Shivam Ragoonaden
#9 March 2014

x = 0
count = 0

y = 2

import math

while x != 2:
    count = count + 1
    x = (math.sqrt(2 + x))
    if count == 1:
        z = y * 2/x
    else:
        z = z * 2/x

zs = round(z,3)
zs = str(zs)

print("Approximation of pi:",zs) 
r = eval(input("Enter the radius:\n"))
a = round(z*r**2,3)
a = str(a)
print("Area:",a) 