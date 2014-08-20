#RSNADA001
#Adam Rosendorff
from math import sqrt
pi = 2
n = sqrt(2)
while n != 2:
    pi *= 2/n
    n = sqrt(2+n)
print('Approximation of pi:',round(pi,3))
radius = eval(input('Enter the radius:\n'))
print('Area:',round(pi*radius**2,3))

