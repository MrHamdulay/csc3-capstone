import math
n=2
d=math.sqrt(2)
product=2
while d<2:
    frac=(n/d)
    product=product*frac
    d=math.sqrt(2+d) 
p=round(product,3)
print("Approximation of pi:",p)
r=eval(input("Enter the radius:\n"))
a=product*r**2
print("Area:",round(a,3))

