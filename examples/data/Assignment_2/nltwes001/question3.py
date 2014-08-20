import math
pie=2
divisor=math.sqrt(2)
while (2/divisor) !=1:
    pie*=2/divisor
    divisor=math.sqrt(2+divisor)
print("Approximation of pi:", round(pie,3))
radius=eval(input("Enter the radius:"'\n'))
area=pie*(radius**2)
print("Area:", round(area,3))

      