import math
a=2
b=2
c=2
while(b/math.sqrt(c) != 1):
    a*=b/math.sqrt(c)
    c=2+math.sqrt(c)
print("Approximation of pi:",round(a,3))
x=eval(input("Enter the radius:\n"))
area=round(a*x*x,3)
print("Area:",area)