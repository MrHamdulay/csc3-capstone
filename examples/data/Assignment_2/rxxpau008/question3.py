import math

denom = math.sqrt(2)
pi = 2
while ((2/denom)!=1):
    pi = pi*(2/denom)
    denom = math.sqrt(2+denom)


print("Approximation of pi:", round(pi,3))
radius = eval(input("Enter the radius:\n"))
print("Area:", round(pi*(radius**2),3))