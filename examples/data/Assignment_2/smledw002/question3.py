import math

value = 2**0.5 
pi_value = 2

while value != 2:
    pi_value = pi_value* (2/value)
    value = math.sqrt( 2 + value)

print("Approximation of pi:", round(pi_value,3))
radius = eval(input("Enter the radius:\n"))
              
area = pi_value * radius**2

print("Area:", round(area,3))
