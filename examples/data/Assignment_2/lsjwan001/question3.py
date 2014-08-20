import math

a=2
b=math.sqrt(2)
x=2
y=0
while y!=1:
    y=a/b
    x=x*y
    b=math.sqrt(2+b)
    
print("Approximation of pi:",round(x,3))
radius=eval(input("Enter the radius:\n"))
    
answer= x*radius*radius
print("Area:",round(answer,3))
    
