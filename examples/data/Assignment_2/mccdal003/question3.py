
from math import*                 
i=2
pi=2*(2/sqrt(2))
x=sqrt(2+sqrt(2))
while i!=1:
    pi=pi*(2/x)
    x=sqrt(2+x)
    i=2/x
    
print("Approximation of pi:",round(pi,3)) 
z=eval(input("Enter the radius:\n"))
answer=pi*z**2

print("Area:",round(answer,3))