#Awande Madonsela
#MDNAWA001
#Assignment

from math import*
x=sqrt(2)
y=2
pi=2*(y/x)

while x<2:
    x=(sqrt(2+x))
    pi=(pi*y/x)
print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
print("Area:",round(pi*r**2,3))
