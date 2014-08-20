import math
x=0
y=0
z=2
while y!=1:
    x=math.sqrt(2+x)
    y=2/x
    z=z*y
print("Approximation of pi:",round(z,3))

r=eval(input("Enter the radius:\n"))
A=z*(r*r)
print("Area:",round(A,3))