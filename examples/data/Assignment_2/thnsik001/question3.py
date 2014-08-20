import math
denom=0
pi=2
count =0
term =1
while term!= 1 or count ==0:
    pi*=term
    denom =math.sqrt(2+denom)
    term=2/denom
    count=+1
print("Approximation of pi:",round(pi,3))
radius = eval(input("Enter the radius:\n"))
area = (radius**2)*pi
print("Area:",round(area,3))