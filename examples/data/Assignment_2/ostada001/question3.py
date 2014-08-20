import math

divisor = math.sqrt(2)
count = 2
pi = 2

while 2/divisor > 1  :
    
    pi = pi*(2/divisor)    
    divisor = math.sqrt(2+divisor)
    
    
print("Approximation of pi:", round(pi,3))
r = eval(input("Enter the radius:\n"))
print("Area:",round((pi)*(r**2),3))