import math

pi = 2 * 2/(math.sqrt(2)) * 2/(math.sqrt(2 + math.sqrt(2))) * 2/(math.sqrt(2 + math.sqrt(2 + math.sqrt(2))))
print("Approximation of pi:",round(pi,3))
rad = eval(input("Enter the radius:\n"))

print("Area:", round(pi*rad**2,3))