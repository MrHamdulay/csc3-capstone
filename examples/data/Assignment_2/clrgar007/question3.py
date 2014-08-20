import math
a=0
num=2
pi=1
while num>1: 
    pi*=num
    b=math.sqrt(2+a)
    a=b
    num=(2/b)

print("Approximation of pi:",round(pi,3))
print("Enter the radius:")
radius=eval(input())
print("Area:", round(pi*radius*radius,3))