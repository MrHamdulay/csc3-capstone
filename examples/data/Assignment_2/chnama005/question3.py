# amanda chonco

from math import*
a=sqrt(2)
b=2
pi=2*(b/a)

while a<2:
    a=sqrt(2+a)
    pi=pi*(b/a)
print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
print("Area:",round(r**2*pi,3))



