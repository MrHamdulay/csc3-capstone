import math

i=math.sqrt(2)
pi = 2
n = 0

while n != 1:
    n = 2/i    
    i = math.sqrt(2+i)
    pi = pi * n

print('Approximation of pi:',round(pi,3))

r=eval(input('Enter the radius:\n'))
area=(pi*r**2)
print('Area:',round(area,3))
