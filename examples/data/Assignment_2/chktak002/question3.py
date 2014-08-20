
import math
z=2
w=0
x=0    
y=2 
while w != 1:   
    x=math.sqrt(2+x)
    z= z * y/x
    w=y/x
zs=round(z,3)
zs = str(zs)
print("Approximation of pi:",zs)

radius =eval(input("Enter the radius:\n"))
area=z*radius**2
area=round(area,3)
area=str(area)
print("Area:",area)