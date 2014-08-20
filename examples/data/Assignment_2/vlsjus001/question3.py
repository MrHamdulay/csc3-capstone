# question 3
# justin valsecchi_VLSJUS001
# 11 march 2014

import math

denom = math.sqrt(2)
pi = 2*2/denom

while (denom != 2):
    denom += 2
    denom = math.sqrt(denom)
    pi *= 2/denom
    
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
print("Area:",round(radius**2*pi,3))



    
    
    
    
