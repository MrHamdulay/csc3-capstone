import math
s=math.sqrt(2)
n=2/s
pi=n*2
while n!=1:
    s=math.sqrt(2+s)
    n=2/s
    pi*=n
print("Approximation of pi:",round(pi,3))

def pii():
    r=eval(input("Enter the radius:\n"))
    area=pi*r**2
    print("Area:",round(area,3))
pii()