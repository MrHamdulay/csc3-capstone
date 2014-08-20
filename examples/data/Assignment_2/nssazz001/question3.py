# finding the value of pi
# Azza Nassor
# NSSAZZ001

import math

x=2
pi=1
a=0
while x>1 :
    pi*=x
    b=math.sqrt(2+a)
    a=b
    x=2/a

print( "Approximation of pi:", round(pi,3))
radius = eval(input("Enter the radius:\n"))
Area = pi*radius**2
print("Area:", round(Area,3))

    
    
   