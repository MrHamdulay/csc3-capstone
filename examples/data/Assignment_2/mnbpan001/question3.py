n=0
import math
x=2/(math.sqrt(2+n))
PI=2
while x !=1:
    PI=PI*x
    n=math.sqrt(n+2)
    x=2/(math.sqrt(2+n))
y=round(PI,3)
print('Approximation of pi:',round(PI,3))
r=eval(input('Enter the radius:\n'))
print('Area:',round(PI*r**2,3))
