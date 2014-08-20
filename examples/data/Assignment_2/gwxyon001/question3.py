import math
a = 2
b = math.sqrt(2)
c = 0
while c!=1:
    c= 2/b
    a= a*c
    b= math.sqrt(2+b)
    
print("Approximation of pi:",round(a,3))
r=eval(input("Enter the radius:\n"))
Area= round(a*r**2, 3)
print("Area:",Area)

