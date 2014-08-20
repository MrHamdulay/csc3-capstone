import math
multiplier = 2
denominator = math.sqrt(2)
pi = 2
while denominator != 2:
    multiplier = 2 / denominator
    pi = pi * multiplier
    denominator = math.sqrt(2 + denominator)
print("Approximation of pi:", round(pi,3))
radius = eval(input("Enter the radius:\n"))
area = pi * radius ** 2
print("Area:", round(area, 3))