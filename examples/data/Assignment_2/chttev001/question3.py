#CHTTEV001
#Author:Tevin Chetty
#question3

from math import sqrt
i=sqrt(2)
pi=2
while 2/i!=1:
    pi*=2/i
    i=sqrt(2+i)
    
    
print("Approximation of pi:",round(pi,3))
rad=eval(input("Enter the radius:\n"))
print("Area:",round(pi*rad**2,3))