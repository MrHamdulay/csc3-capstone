import math
x=2
y=2
z=2
while (x/math.sqrt(y)!=1):
    z*= x/math.sqrt(y)
    y=2+math.sqrt(y)

print("Approximation of pi:", round(z,3))
r=eval(input("Enter the radius:\n"))
area=round(z*r*r,3)
print("Area:",area)