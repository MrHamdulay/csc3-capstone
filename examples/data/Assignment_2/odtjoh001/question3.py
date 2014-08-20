import math
num = 2
mult = 2
pi = 2
x = 0
while(num/ math.sqrt(mult)!= 1):
    pi *= num / math.sqrt(mult)
    mult = 2 + math.sqrt(mult)

print("Approximation of pi:", round(pi,3))
radius = eval(input("Enter the radius:\n"))
area = round(pi * (radius * radius),3)
print("Area:", area)