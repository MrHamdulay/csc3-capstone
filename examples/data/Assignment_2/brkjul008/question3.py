#finding pi
#Julia Breakey

import math

num=2
pi=1
a=0
while num>1:
    pi*=num
    b=math.sqrt(2+a)
    a=b
    num=2/b
    
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=pi*(radius**2)
print("Area:", round(area,3))