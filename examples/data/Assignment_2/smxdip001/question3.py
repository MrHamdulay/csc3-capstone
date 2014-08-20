import math
c=0
d=1
while c!=2:
    c=math.sqrt(2+c)
    d=(2/c)*d
    e=2*d
print("Approximation of pi:",round(e,3))
x=eval(input("Enter the radius:\n"))
area=round(e*(x**2),3)
print("Area:",area)
