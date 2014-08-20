import math
pi=2
constant=math.sqrt(2)
while (2/constant)!=1:
    pi*=2/constant
    constant=math.sqrt(2+constant)
print("Approximation of pi:", round(pi,3))
radius = float(input("Enter the radius: \n"))
area = pi*(radius**2)
print("Area:", round(area,3))
        
         
