#program to calculate the value of PI
#Tayla George
#13 March 2014

import math

x= math.sqrt(2)
pi =2*(2/x)

while x !=2:
    x = math.sqrt(2+x)
    pi = pi*(2/x)
print("Approximation of pi:",round(pi,3))
radius = eval(input("Enter the radius:\n"))
area = (pi*(radius**2))
print("Area:",round(area,3))