import math
i=math.sqrt(2)
y=2*2/i
while i !=2:
    i=math.sqrt(2+i)
    y=y*2/i
round(y,3)
print("Approximation of pi:",round(y,3))
r=eval(input("Enter the radius:\n"))
print("Area:",round(r*r*y,3))

