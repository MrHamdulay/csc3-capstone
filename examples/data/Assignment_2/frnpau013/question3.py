import math
pi = 2 
newterm = 2
count = 0

while newterm > 1:
    sqrt = math.sqrt(2)
    for i in range(count):
        sqrt = math.sqrt(2 + sqrt)
    newterm = 2/sqrt
    pi = pi * newterm
    count += 1


print("Approximation of pi:", round(pi, 3))
radius = eval(input("Enter the radius:\n"))
area = pi * radius**2
rounding = round(area, 3)
print("Area:", rounding)

