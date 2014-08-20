import math
x=math.sqrt(2)
y=2*(2/(math.sqrt(2)))
while (2/x)>1:
    x=math.sqrt(x+2)
    d=y*(2/x)
    y=d
    
print("Approximation of pi:",round(d,3))
m=eval(input("Enter the radius:\n"))
area=d*m**2
print("Area:",round(area,3))