import math
a=math.sqrt(2)
p=2*(2/a)
while(a!=2):
    a=math.sqrt(2+a)
    p=p*(2/a)
print("Approximation of pi:",round(p,3))
r=eval(input("Enter the radius:\n"))
print("Area:",round((p*(r**2)),3))
    
     