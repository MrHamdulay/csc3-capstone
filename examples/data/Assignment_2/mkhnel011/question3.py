import math
pi=2
constant=math.sqrt(2)
a = 2/constant
while a !=1:
    pi= pi * a
    constant=math.sqrt(2+constant)
    a = 2/constant
    
print("Approximation of pi:",str(round(pi,3)))
radius=eval(input("Enter the radius:\n"))
area= pi*(radius**2)
print("Area:",round(area,3))