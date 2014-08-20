import math
PI=2
incr=0
temp=0
counter=0
z=0
while(temp!=1):
    temp=2/(math.sqrt(2+incr))
    PI*=temp
    incr=math.sqrt(2+z)
    z=incr

print("Approximation of pi:",round(PI,3))
radius=float(input("Enter the radius:\n"))
area=PI*(radius**2)
print("Area:",round(area,3))