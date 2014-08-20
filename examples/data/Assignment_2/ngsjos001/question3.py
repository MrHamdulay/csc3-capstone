import math
a=2
b=math.sqrt(2)
c=math.sqrt(a+b)
d=math.sqrt(a+c)
e=math.sqrt(a+d)
f=math.sqrt(a+e)
g=math.sqrt(a+f)
h=math.sqrt(a+g)
i=math.sqrt(a+h)

pi=(2**9)*(b**-1)*(c**-1)*(d**-1)*(e**-1)*(f**-1)*(g**-1)*(h**-1)*(i**-1)

print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
area=(pi)*(r**2)
print("Area:", round(area,3))