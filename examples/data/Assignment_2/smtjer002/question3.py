#This is a program to approximate pi and then to determine the area of a circle
# Author: Jeremy Smith
# Student Number: SMTJER002

import math
numerator = 2
denominator = math.sqrt(2)
n = numerator / denominator
sumPI = 2 * 2 / math.sqrt(2)
while n > 1:
    denominator = math.sqrt(2 + denominator)
    sumPI = sumPI * 2 / denominator
    n = 2 / denominator
   
print("Approximation of pi: ", end="")
print(round(sumPI,3))
radius = eval(input("Enter the radius:\n"))
area = sumPI*radius**2
print("Area: ", end="")
print(round(area,3))