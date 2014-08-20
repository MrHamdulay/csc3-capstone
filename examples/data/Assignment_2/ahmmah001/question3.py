#Calculating pi and area
#Mahnoor Ahmed
#AHMMAH001

import math
x=math.sqrt(2)
y=2/x
for i in range(120):
    x=math.sqrt(2+x)
    y=y*2/x

pi=2*y
    
print("Approximation of pi:",round(pi, 3))
r=eval(input("Enter the radius:\n"))
a=pi*r**2
a=round(a,3)
print("Area:",a)
    