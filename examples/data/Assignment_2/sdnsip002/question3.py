
import math

x = math.sqrt(2)
pi = 2*(2/x)
while x!= 2: #denominator x has to equal to 2 for the size of the term to be 1.
    x  = math.sqrt(2+x)
    pi = (pi*(2/x))

print("Approximation of pi:", round(pi,3))
y=eval(input("Enter the radius:\n"))
print("Area:", round((pi*(y**2)),3))
