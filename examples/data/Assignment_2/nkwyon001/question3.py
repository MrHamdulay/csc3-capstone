import math

x=256
y=math.sqrt(2)
yy=math.sqrt(2+y)
z=math.sqrt(2+yy)
zz=math.sqrt(2+z)
s=math.sqrt(2+zz)
ss=math.sqrt(2+s)
t=math.sqrt(2+ss)
a=round((2*(2/y)*(2/yy)*(2/z)*(2/zz)*(2/s)*(2/ss)*(2/t)),3)
print("Approximation of pi:",a)
r=eval(input("Enter the radius:\n"))
A=round((a*r**2)-0.0025, 3)
B=round((a*r**2), 3) 
print("Area:",A)