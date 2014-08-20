#question 3
#By: Dean de Haast

import math

pi = 2
dnom= math.sqrt(2)
pi = pi*(2/dnom)

while dnom !=2:
    dnom= math.sqrt(dnom+2)
    pi = pi*(2/dnom)
   
    
piround=round(pi,3)

print("Approximation of pi: " + str(piround))
radius = eval(input("Enter the radius:""\n"))
area = round((pi*(radius**2)),3)

print("Area: "+str(area))
