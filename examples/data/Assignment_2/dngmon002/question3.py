import math
p=0
prox=2
nxt=0
while nxt!=1:
    p=math.sqrt(2+p)
    prox*=2/p
    nxt=2/p
print("Approximation of pi:",round(prox,3))
radius=eval(input("Enter the radius:\n"))
area= prox*(radius**2)
print("Area:",round(area,3))
