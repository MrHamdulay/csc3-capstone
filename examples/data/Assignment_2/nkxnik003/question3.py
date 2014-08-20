#PI Program
#Nikhil Jiten Naik (NKXNIK003)
#8th of March 2014

import math
x = 2
pi = math.sqrt(2)
while (2/pi) != 1:
    x *= 2/pi
    pi = math.sqrt(2 + pi)
    
print("Approximation of pi:", round(x, 3))
rad = float(input("Enter the radius:\n"))
print("Area:", round(x * rad**2, 3))