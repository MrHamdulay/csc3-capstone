#Phillip Ruhesi
import math
y=math.sqrt(2)
x=2
denom=math.sqrt(2)
pi=2
while denom<2:
    term=(2/denom)
    pi*=term
    denom=math.sqrt(denom+2)

print('Approximation of pi:',round(pi,3))
r=eval(input('Enter the radius:\n'))
a=pi*(r**2)
print('Area:',round(a,3))
