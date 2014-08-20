#Calculate pi
import math

product = math.sqrt(2)
pi = 2

while 2/product != 1:
    pi = pi*(2/product)
    product = math.sqrt(2+product)
    
print("Approximation of pi:", round(pi, 3))
rad = eval(input("Enter the radius:\n"))
area = pi*(rad**2)
print("Area:", round(area,3))



