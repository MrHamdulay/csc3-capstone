#Program to calculate pi

import math

x = math.sqrt(2)
a=1
while True:
    a=a*2/x
    x=math.sqrt(x+2)
    if 2/math.sqrt(x+2)==math.factorial(1):
        break
pi = (2*a)
print ("Approximation of pi: ", round(pi, 3), sep="")
radius = eval(input("Enter the radius:\n"))
area = pi*radius**2
print ("Area: ", round(area, 3), sep="")