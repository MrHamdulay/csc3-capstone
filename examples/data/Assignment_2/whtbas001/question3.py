#ASSIGNMENT 2
#QUESTION 3
#WHTBAS001
#BASIL T WHITEHEAD
#10-03-2014

import math

i = 0
x = 2

while i != 2:
    i = math.sqrt(2 + i)
    x = (x*2)/i
    i = round(i, 16)

print("Approximation of pi:",round(x,3), end="\n")

def area():
    radius = eval(input("Enter the radius:\n"))
    area = x*(radius**2)
    print("Area:",round(area, 3))
area()