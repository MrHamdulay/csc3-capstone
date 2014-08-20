#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lungelo
#
# Created:     08/03/2014
# Copyright:   (c) Lungelo 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
incr=0
pi=2
bottom=0
nextTerm=0
while nextTerm!=1:
    incr=bottom
    bottom=((2+incr)**(1/2))
    nextTerm=2/bottom
    pi=pi*nextTerm

print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
Area=pi*(radius)**2
print("Area:",round(Area,3))






