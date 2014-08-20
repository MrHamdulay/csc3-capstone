#Assignment2 q3

import math

denom = 2**0.5
ans = 2  

while denom != 2:
    newterm = 2/denom    
    denom=(2+denom)**0.5
    ans = ans * newterm
    
    
print("Approximation of pi:", round(ans,3))

radius = eval(input("Enter the radius:\n"))

area = ans * radius**2

print("Area:", round(area,3))