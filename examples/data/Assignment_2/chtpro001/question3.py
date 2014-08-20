import math
b=math.sqrt(2)
pi=2
while b!=2:
        pi=pi*(2/b)
        b=math.sqrt(2+b)
print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
print("Area:",round(pi*r*r,3))

    