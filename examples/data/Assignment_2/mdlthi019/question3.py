import math

a = 2
b = 0
while b!= 1:
    b = math.sqrt(2+b)
    a = a*(2/b)
    if (2/b)==1:
        break
print("Approximation of pi:", round(a,3))
radius = eval(input("Enter the radius:\n"))
area = a*radius**2
print("Area:", round(area,3))


