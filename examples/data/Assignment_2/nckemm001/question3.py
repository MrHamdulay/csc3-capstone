import math
circle =math.sqrt(2)
square=2

while(circle<2):
    square=square*(2/circle)
    circle=math.sqrt(2+circle)
    
print("Approximation of pi:",round(square,3))
pi=eval(input("Enter the radius:\n"))
print("Area:",round(square*pi*pi,3))