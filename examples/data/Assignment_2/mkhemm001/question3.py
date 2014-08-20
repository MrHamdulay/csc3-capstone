import math
a=2
d=math.sqrt(2)
x=a/math.sqrt(2)
p=a
while x>1:
    p=p*x
    d=math.sqrt(2+d)
    x=a/d
print("Approximation of pi:",round(p,3))
r=eval(input("Enter the radius:\n"))
print("Area:",round(p*r*r,3))