import math
pi = 2
divisor = math.sqrt(2)
newterm = 2/math.sqrt(2)
while newterm != 1 :
    pi *= newterm
    divisor = math.sqrt(2+divisor)
    newterm = 2/divisor
print("Approximation of pi:",str(round(pi,3)))
radius = eval(input("Enter the radius:\n"))
print("Area:",str(round(pi*radius*radius,3)))