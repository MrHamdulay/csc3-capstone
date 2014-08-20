import math

a=0
b=2
p=1
while b > 1:
    if a==0:
        a=math.sqrt(2+a)#a=root2
        p=p*b# p=2
    else:
        b=2/a
        a=math.sqrt(2+a)
        p=p*b
print("Approximation of pi:",round(p,3))
r=eval(input("Enter the radius:\n"))
Area=p*(r**2)
print("Area:",round(Area,3))
