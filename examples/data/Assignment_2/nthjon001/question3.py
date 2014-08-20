import math
pi=2
denom=math.sqrt(2)
for i in range(1,99999):
    pi*=(2/denom)
    denom=math.sqrt(denom + 2)
print("Approximation of pi:", round(pi,3))
radius=eval(input("Enter the radius:\n"))
print("Area:", round((radius**2 * pi), 3))
    