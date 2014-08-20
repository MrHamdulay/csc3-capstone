import math

pi = 2
b = math.sqrt(2)
a = 2/b

while a != 1:
    pi = pi * a
    b = math.sqrt(2 + b)
    a = 2/b

print("Approximation of pi:", round(pi,3)) 
r = eval(input("Enter the radius:\n"))
Area = round(pi * (r**2),3)
print("Area:", Area)