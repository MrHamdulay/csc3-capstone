from math import *
y = sqrt(2)
x = 0
rpi = 2*y
rcount = 0
while x != 1:
    rcount += 1
    y = sqrt(2 + y)
    x = 2/y
    rpi *= x    
print("Approximation of pi:",round(rpi,3))
rradius = eval(input("Enter the radius:\n"))
print("Area:",round((rradius**2)*rpi,3))