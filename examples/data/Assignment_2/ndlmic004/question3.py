#question 3
#Michell Ndlozi

from math import*
m= sqrt(2)
n=2
pi=2*(n/m)
    
while m<2:
        m=(sqrt(2+m))
        pi=(pi*n/m)         
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
print("Area:",round(pi*radius**2,3))
