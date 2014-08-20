import math
a=0
b=1
while a!=2:
    a=math.sqrt(2+a)
    b=(2/a)*b 
    c=2*b
print("Approximation of pi:",round(c,3))
x=eval(input("Enter the radius:\n"))
area=round(c*(x**2),3)
print("Area:",area)