import math

total=2*(2/(math.sqrt(2)))
denom=math.sqrt(2)

while((2/denom)!=1):
 denom=math.sqrt(2+denom)
 total*=(2/denom)
 
print("Approximation of pi:",round(total,3))
radius=eval(input("Enter the radius:\n"))
print("Area:",round((total*radius**2),3))