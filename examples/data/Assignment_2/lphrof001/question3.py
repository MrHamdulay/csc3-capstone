import math

r=math.sqrt(2)
pie=2*(2/r)

while (r!=2):
        r=math.sqrt(2+r)
        pie*=(2/r)


print("Approximation of pi:",round(pie,3))
x=eval(input("Enter the radius:\n"))
radius=x**2
Area=radius*pie
print("Area:",round(Area,3))
       