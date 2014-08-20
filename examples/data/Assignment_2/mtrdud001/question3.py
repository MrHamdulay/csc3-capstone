from math import *
num=2
den=sqrt(2)
pi=2
while((num/den)>1):
    pi*=(num/den)
    den=sqrt(2+den)

print("Approximation of pi:",round (pi,3))
a=eval(input("Enter the radius:\n"))
area2= round(pi,4)*a*a
print("Area:",round(area2,3))
    
    