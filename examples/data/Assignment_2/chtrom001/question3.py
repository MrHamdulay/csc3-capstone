from math import *
i=sqrt(2)
a=2/i
pi=2*a

while a!=1:
    i=sqrt(2+i)
    a=2/i
    pi*=a
    
print("Approximation of pi:",round(pi,3))
t=eval(input("Enter the radius:\n"))
area= pi*t**2
print("Area:",round(area,3))