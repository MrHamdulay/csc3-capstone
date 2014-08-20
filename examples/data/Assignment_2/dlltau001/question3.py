#Question3
import math

initial = 2 * (2 / math.sqrt(2))
numerator = 2
term = 0
denominator = 0
pi = 1

while term != 1.0:
    denominator = math.sqrt(2 + denominator)
    term = numerator / denominator
    pi = term * pi
   

pi = pi * 2
approximatepi = round(pi,3)

print("Approximation of pi:",approximatepi)
radius = eval(input("Enter the radius:\n"))
area = (pi * (radius * radius))
print("Area:",round(area,3))
    
    
