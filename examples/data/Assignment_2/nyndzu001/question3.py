import math
z=0
y=math.sqrt(2)
w=2
while z!=1:
    z=(2/y)
    w=w*z
    y=math.sqrt(2+y)
    if z==1:
        print("Approximation of pi:",round(w,3))
        r=eval(input("Enter the radius:\n"))
        print("Area:",round((w*r**2),3))