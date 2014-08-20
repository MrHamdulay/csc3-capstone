# Area of a circle

import math
 
pi_approx = 2.00
den = 0.00
 
while (den != 2):
    den = math.sqrt(2 + den)
    pi_approx = pi_approx * 2 / den
     
print ("Approximation of pi:%6.3f" %pi_approx)

r = eval(input("Enter the radius:\n"))
a=(pi_approx*r**2)
print("Area:",round(a,3))
