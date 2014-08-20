import math
x = math.sqrt(2)
y = 2/math.sqrt(2)
z = 2

while y > 1:
    z = z*y
    x = math.sqrt(2+x)
    y = 2/x

print("Approximation of pi:", round(z, 3))
radius = eval(input("Enter the radius:\n"))
area = round(z*radius**2, 3)
print("Area:", area)

