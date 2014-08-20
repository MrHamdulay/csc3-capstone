import math
#initialize variables
divisor = 0
pi_approx = 2
factor = 2
#Finding a approximation for pi
while (factor > 1):
    divisor = math.sqrt(2 + divisor)
    factor = 2/divisor
    pi_approx *= factor

print("Approximation of pi:", round(pi_approx,3), sep = " ")
radius = eval(input("Enter the radius:\n"))
area = pi_approx * (radius**2)
print("Area:", round(area,3), sep = " ")