import math
x = math.sqrt(2)
t=2
y=2
while t!=1:
    t=2/x
    x = math.sqrt(2 + x)
    y=y*t
print("Approximation of pi:",(round((y),3)))
g= eval(input("Enter the radius:\n"))
d= (y)*g*g
print("Area:",(round(d,3)))
    
    