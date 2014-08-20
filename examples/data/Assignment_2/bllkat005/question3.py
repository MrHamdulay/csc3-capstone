#BLLKAT005
#Kate Bell
#11 March 2014

import math
x=math.sqrt(2)
pi_approx=2

while(x<2):
    pi_approx=pi_approx*(2/x)
    x=math.sqrt(2+x)
    
print("Approximation of pi:",round(pi_approx,3))

r= eval(input("Enter the radius:\n"))
print("Area:",round(pi_approx*r*r,3))


    
