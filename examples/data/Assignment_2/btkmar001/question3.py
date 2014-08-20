import math
term = 2
denom = math.sqrt(2)
while denom<2:
    term = term * (2/denom)
    denom = math.sqrt(2+denom)
print("Approximation of pi:",round(term,3))
radius = eval(input("Enter the radius:\n"))
print("Area:", round((radius**2)*term,3))