import math
x=math.sqrt(2)
y=2
while (2/x)!=1:
    y=y*(2/x)
    x=math.sqrt(2+x)
print("Approximation of pi:",round(y,3))
z=eval(input("Enter the radius:\n"))
print("Area:", (round((y)*(z**2),3)))