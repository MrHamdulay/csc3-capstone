import math
a=0
b=0
c=1
pi=2
while c!=1 or b==0:
    pi*=c
    a=math.sqrt(2+a)
    c=2/a
    b=1
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=radius**2*pi
print("Area:",round(area,3))