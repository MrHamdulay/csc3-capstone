#Pi program
#Robin Hall
#14/03/2014

import math
  
def denom(x):
    if x == 0:
        return 0
    return (2 + math.sqrt(denom(x-1)))
    
def series(x):
    if x == 0:
        return 2
    denom_full = math.sqrt(denom(x))
    return 2/denom_full
    
x=0
pi=1
while series(x) !=1:
    pi*=series(x)
    x+=1
    
print ("Approximation of pi:", round(pi, 3))
radius = eval(input("Enter the radius:\n"))
    
area = pi*radius**2
print ("Area:", round(area, 3))

    