import math
pi = 1
den = 0
nxt = 0
i = 1
while nxt != 1:
    if i == 1:
        pi *=2
    else:
        den = math.sqrt(2+den)
        nxt = 2/den
        pi *= nxt
    i -=1    
print("Approximation of pi:",round(pi,3))
radius = eval(input("Enter the radius:\n"))
area = pi*(radius**2)
print("Area:",round(area,3))