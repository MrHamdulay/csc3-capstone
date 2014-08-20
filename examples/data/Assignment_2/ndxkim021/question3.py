import math

pi = 0
deno = math.sqrt(2)
pi = 2 * (2 / deno)

while deno!=2:
    deno = math.sqrt(2+deno)
    pi = pi * (2 / deno)
    
print("Approximation of pi:", round(pi,3))
radius  = eval(input("Enter the radius:\n"))
area = pi * radius * radius
print("Area:",round(area,3))

