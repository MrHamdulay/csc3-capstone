# question3
# a program that calculates the value of PI and then computes and displays 
#   the area of a circle with radius entered by the user.
# Thomas Konigkramer
# 8 March 2014

import math

approximation = 2
denominator = math.sqrt(2)

while denominator < 2:
    approximation = approximation * 2/denominator
    denominator = math.sqrt(2 + denominator)
    
print("Approximation of pi:", round(approximation, 3))

radius = eval(input("Enter the radius:\n"))

area = approximation * radius**2

print("Area:", round(area, 3))