import math
x = 2
y = 0
z = 0
pi = 2
i = 0
while i<= 10:
    i = i -1
    y = math.sqrt(x + y)
    z = x/y
    pi = pi * z
    if z <= 1:
        break
        
    
print("Approximation of pi:" , round(pi,3), end = "\n")
radius = eval(input("Enter the radius:\n"))
area = round(pi * radius * radius,3)
print("Area:", area)