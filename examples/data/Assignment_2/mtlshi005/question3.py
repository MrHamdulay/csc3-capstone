#08/03/2014
#Shivaan Motilal
#Programme to calculate area of a circle

from math import *
i=2
pi=2*(2/sqrt(2))
btm=sqrt(2+sqrt(2))
while i!=1:
    pi=pi*(2/btm)
    btm=sqrt(2+btm)
    i=2/btm

    


print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=pi*(radius)**2
area=round(area,3)
print("Area:",area)

#y=eval(input("Enter the radius:")
#%print("Area:",area")