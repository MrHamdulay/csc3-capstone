# A program that calculates the value of PI and then computes and displays the area of a circle
# Themba Mtsweni
# 2013/03/22

import math

oldpi = 0
pi = 2
denominator = math.sqrt(2)

while (pi != oldpi):
    oldpi = pi
    pi = pi* 2 / denominator
    denominator = math.sqrt(2 + denominator)


print("Approximation of pi:",round(pi,3))

radius = eval(input("Enter the radius:\n"))

Area = ((pi) * (radius**2))

print("Area:",round(Area, 3))