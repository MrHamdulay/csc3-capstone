from math import *
pi=2
lastT=sqrt(2)
while 2/lastT!=1:
    pi*=2/lastT
    lastT=sqrt(2+lastT)
    
print("Approximation of pi:",round(pi,3))

rad=eval(input("Enter the radius:"))
print("")
Area=pi*rad*rad
print("Area:",round(Area,3))
