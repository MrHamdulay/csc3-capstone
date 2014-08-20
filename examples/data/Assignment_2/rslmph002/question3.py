import math

total = 1
denom = math.sqrt(2)
newdenom = math.sqrt(2+denom)

while newdenom < 2:
    print("Approximation of pi: ",round(newdenom*2,3))
    break

x = eval(input("Enter a radius:\n"))
area = (x*x*newdenom)

print("Area: ",round(area,3))