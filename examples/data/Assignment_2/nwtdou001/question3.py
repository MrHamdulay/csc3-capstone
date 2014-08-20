import math

pi = 2
base = math.sqrt(2)

for x in range(0,1000):
    pi = pi * (2/base)
    base = math.sqrt(2+base)

print("Approximation of pi:",round(pi,3))
radius = eval(input("Enter the radius:\n"))
print("Area:",round(pi*radius*radius,3))