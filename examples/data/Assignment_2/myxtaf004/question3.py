#Author: Moyo, Tafadzwa
#Student Number: MYXTAF004

import math
n=math.sqrt(2)
x=2
pi=2
for i in range(100): 
    pi=pi*(2/n)
    n=math.sqrt(2+n)
pia=round(pi, 3)
print("Approximation of pi:",pia)
r=eval(input("Enter the radius:\n"))
a=round(r**2*pi, 3)
print("Area:", a)