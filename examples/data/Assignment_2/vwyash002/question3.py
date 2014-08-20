# assignment 2 question 3
# VWYASH002

import math
denom=math.sqrt(2)
pi=2
while denom<2:
    pi=pi*(2/denom)
    denom=math.sqrt(2+denom)
print( "Approximation of pi:",(round (pi,3)) )
r=eval(input("Enter the radius:\n"))
ans=pi*r**2
print("Area:", round(ans,3))