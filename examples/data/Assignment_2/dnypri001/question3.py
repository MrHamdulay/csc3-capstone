import math
a=2
b=math.sqrt(2)
n=a*(a/b)
while b !=2:
  b=math.sqrt(a+b)
  n=n*(a/b)
pass  
print("Approximation of pi:",round(n,3))
radius=eval(input("Enter the radius:\n"))
area= n*radius**2
print("Area:",round(area,3))
