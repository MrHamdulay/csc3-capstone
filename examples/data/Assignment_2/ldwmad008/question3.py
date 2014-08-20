import math
pi=2
x=2
y=2
z=math.sqrt(2)
while y>1:
    x=math.sqrt(x)
    y=2/x
    x=2+z
    z=math.sqrt(2+z)
    pi=pi*y
print('Approximation of pi:', round(pi, 3), sep=' ')
r=eval(input("Enter the radius:\n"))
print('Area:', round(pi*(r**2), 3), sep=' ')