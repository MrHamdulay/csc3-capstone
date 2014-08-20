import math
x=math.sqrt(2)
y=2
while 2/x >1:
    y=y*2/x 
    x=math.sqrt(2+x)
    PI=round(y,3)
    
print("Approximation of pi:",PI)
z=eval(input("Enter the radius:\n"))
Area=y*z**2
A=round(Area, 3)
print("Area:", A)