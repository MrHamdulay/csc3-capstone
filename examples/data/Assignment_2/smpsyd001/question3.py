
from math import*
y=sqrt(2)
i=2
while y<2:
    i=i*(2/y)
    y=sqrt(2 + y)
    
print ("Approximation of pi:",round(i,3))
r=eval(input("Enter the radius:\n"))
a=(i*r*r)
print("Area:",round(a,3))
