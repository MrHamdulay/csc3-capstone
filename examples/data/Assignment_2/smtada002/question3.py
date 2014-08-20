import math

pi = 2
denom = math.sqrt(2)

while(denom != 2):
    
    pi = pi*(2/denom)
    denom = math.sqrt(2 + denom)

print("Approximation of pi:", round(pi,3))

rad = eval(input("Enter the radius:\n"))

print("Area:", round(pi*rad**2,3))
