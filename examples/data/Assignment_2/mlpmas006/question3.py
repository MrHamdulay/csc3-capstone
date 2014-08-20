import math
x=2
pi=0
abti=0
w=math.sqrt(2)
while abti!=1:
    x*=2/w
    w=math.sqrt(2+w)
    pi=x
    abti=2/w   
print("Approximation of pi:",round(pi,3))
m=eval(input("Enter the radius:\n"))
area=round(pi,4)*m*m
print("Area:",round(area,3))
