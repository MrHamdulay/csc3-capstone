#kennedy muranda
#area of a circle
import math
pi=2

divisor =math.sqrt(2)

while divisor!=2:
    
    pi = pi * 2/divisor
    
    divisor = math.sqrt(2+divisor)
    
    
    
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
print("Area:",round((radius*radius*pi),3))

    
    
    
