# Assignment 2 question 3
# Amy Brodie
# 13/03/2014

import math
term = 0
pitotal = 2
denominator = math.sqrt(2)

while term != 1:
    term = 2/denominator
    pitotal = pitotal * term
    denominator = math.sqrt(2 + denominator)
print("Approximation of pi:", round(pitotal,3)) 

radius = eval(input("Enter the radius:\n"))
area = pitotal*radius**2
print("Area:", round(area,3))