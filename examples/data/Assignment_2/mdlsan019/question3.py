#Name: Sanele Mdlalose
#Student number:MDLSAN019
#Date:12 March 2014
#Question3,Assignment 2

from math import*
def areaofcircle():
    a=2
    b=sqrt(2)
    while b<2:
        a=a*(2/b)
        b=sqrt(2+b)
    pi=a
    print("Approximation of pi:", round(pi,3))
    radius=eval(input("Enter the radius:\n"))
    radius2=radius**2
    area=pi*radius2
    print("Area:", round(area,3))
areaofcircle()

