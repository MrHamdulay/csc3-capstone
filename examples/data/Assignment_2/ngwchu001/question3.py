from math import*
p=2
y=sqrt(2)
while(2/y!=1):
    p=p*2/y
    y=(sqrt(2+y))
print("Approximation of pi:",round(p,3))
pp=eval(input("Enter the radius:\n"))  
area=p*pp**2
area0=round(area,3)
print("Area:",area0)
