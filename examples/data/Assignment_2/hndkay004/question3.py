import math
a=2
b=math.sqrt(2)
while (2/b)!=1:
    a*=2/b
    b=math.sqrt(2+b)
pi= round(a,3)
aprx="Approximation of pi:"
print(aprx,pi)
r=eval(input("Enter the radius:"'\n'))
A=a*r*r
Area= "Area:"
print(Area,round(A,3))

       
