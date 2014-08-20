import math
PI=2
x=math.sqrt(2)
while (2/x >1):
    PI=PI*(2/x)
    x=math.sqrt(2+x)
print('Approximation of pi:',round(PI,3))
radius=eval(input('Enter the radius:\n'))
area=PI*(radius**2)
print('Area:',round(area,3))
