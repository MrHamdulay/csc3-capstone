# A programme that calculates aproximation of PI and calculates area of circle
# Created by: Jenna Lake
# Date: 7/3/2014

import math

x=math.sqrt(2)
count=2.0*(2/(math.sqrt(2)))
while x:
    x=math.sqrt(2+x)
    count= (2/x)*count
    if (2/(math.sqrt (2+x)))==1:
        break
pi=(round(count*1000))/1000
print("Approximation of pi:", pi)

r=eval(input("Enter the radius:\n"))
area=count*r**2
round_area=(round(area*1000))/1000
print("Area:", round_area)
