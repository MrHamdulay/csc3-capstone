import math

pi=2
dem=math.sqrt(2)

while 2/dem >1:
    pi=pi*2/dem
    dem=math.sqrt(dem+2)    
    
x=round(pi,3)

print("Approximation of pi:",x)
r=eval(input("Enter the radius: \n"))
Area=pi*r**2
Area=round(Area,3)
print("Area:", Area)
       






