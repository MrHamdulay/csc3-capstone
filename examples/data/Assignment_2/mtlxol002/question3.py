import math
pi=2
x=math.sqrt(2)
while x<2:
    pi=pi*(2/x)
    x=math.sqrt(x+2)
print("Approximation of pi:", round(pi,3))
r=eval(input("Enter the radius:\n"))
area=pi*r*r
print("Area:", round(area, 3))
