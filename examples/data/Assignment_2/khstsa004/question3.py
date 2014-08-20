# Khosa Tsakiso
# KHSTSA004

from math import*
z=sqrt(2)
y=2
pi=2*(y/z)

while z<2:
    z=(sqrt(2+z))
    pi=(pi*y/z)
print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
print("Area:",round(r**2*pi,3))