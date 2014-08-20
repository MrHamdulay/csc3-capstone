import math
pi=2
x=0
a=math.sqrt(2+x)
while a!=2:
    a=math.sqrt(2+x)
    x=a
    y=2/a
    pi=pi*y
print("Approximation of pi:",round(pi,3))
z=eval(input("Enter the radius:\n"))
q=pi*z**2
w=round(q,3)
print("Area:",w)