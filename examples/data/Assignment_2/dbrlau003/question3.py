#calculate for pi
import math
pi=2
x=0
term=0
while term!=1:
    x=math.sqrt(2+x)
    term=2/x
    pi=pi*term
print("Approximation of pi:",round(pi, 3))
radius=eval(input("Enter the radius:\n"))
area=round(pi*(radius**2), 3)
print("Area:", area)