import math
x=math.sqrt(2)
pi=2*(2/x)
while x!= 2:
    x=math.sqrt(2+x)
    pi=pi*(2/x)
    b=round(pi,3)
print('Approximation of pi:',b)
r =eval(input('Enter the radius: \n'))
area = pi*(r**2)
print('Area:',round(area,3))