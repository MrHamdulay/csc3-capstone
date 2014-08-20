import math

x=2
z=math.sqrt(2)
i=2/z
while x:
    if i==1: break
    x=x*i
    z=math.sqrt(2+z)
    i = 2/z
print("Approximation of pi:",round(x,3))    
radius=eval(input("Enter the radius:\n"))
area=x*(radius**2)
print("Area:",round(area,3))

          