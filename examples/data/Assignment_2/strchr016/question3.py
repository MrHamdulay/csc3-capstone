import math
a,b=0,1
while a!=2:
 a=math.sqrt(2+a)
 b=(2/a)*b
 for i in range(1,2):
  c=2*b*(i/i)
print("Approximation of pi:",round(c,3))
r=eval(input("Enter the radius:\n"))
print("Area:",round(c*(r**2),3))