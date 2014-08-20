# Matthew Finlayson - FNLMAT001
# 09/03/14
# Question 3

import math

x = 0
pi = 2
nextTerm = 0
while (nextTerm != 1):
    x = math.sqrt(2+x)
    nextTerm = 2/(x)
    pi *= nextTerm

print("Approximation of pi:", round(pi, 3))
radius = float(input("Enter the radius:\n"))

area = pi*radius*radius               
print("Area:", round(area,3))