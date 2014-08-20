import math
y=2
x=math.sqrt(2)
while x!=2:
    y= y*(2/x)
    x=math.sqrt(2+x)
print("Approximation of pi:",round(y,3))
rad=eval(input("Enter the radius:\n"))
area=(y*(rad)**2)
print("Area:",round(area,3))