x=0
y=2
pi=1
import math
while y!=1:
    if x==0:
        x=math.sqrt(2+x)
        pi=pi*y
    else:
        y=2/x
        x=math.sqrt(2+x)
        pi=pi*y
#pi=round(pi,3)
print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
area=pi*(r**2)
area=round(area,3)
print("Area:",area)