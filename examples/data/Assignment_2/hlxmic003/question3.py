# Michaela Heale
# Assignment 2 Question 3

import math 

pi = 2
rad = False
denom = 0
sum = 0
while denom!=1:
    sum = 2+math.sqrt(sum)
    denom = 2/math.sqrt(sum)
    pi = pi*denom

print("Approximation of pi:",(round(pi,3)))
rad = eval(input("Enter the radius:\n"))
area = pi*(math.pow(rad,2))
print("Area:",round(area,3))

