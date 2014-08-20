import math 

quotient = 2
y = 0

while y!= 2:
    y = math.sqrt(y + 2)
    quotient = quotient * 2/y
    
print("Approximation of pi:",round(quotient,3))
Radius = eval(input("Enter the radius:\n"))
Area = quotient*(Radius)**2 
print("Area:",round(Area,3))