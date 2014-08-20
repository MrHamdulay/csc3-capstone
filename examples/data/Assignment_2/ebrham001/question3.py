import math


deno = math.sqrt(2)
pi = 2
while 2/deno != 1:
                pi = pi * (2/deno)
                deno = math.sqrt(2 + deno)
print("Approximation of pi:",round(pi,3))      
radius=eval(input("Enter the radius:\n"))
area=(pi*(radius*radius))
print("Area:",round(area,3))
        
      