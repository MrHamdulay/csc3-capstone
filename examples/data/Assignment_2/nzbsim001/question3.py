from math import *

pi = 2
dem = sqrt(2)

while (2/dem != 1):
    pi *= 2/dem
    dem = sqrt(2 + dem)

print('Approximation of pi:',round(pi,3))

x = eval(input( 'Enter the radius:\n'))
area= pi*x*x

print('Area:',round(area,3))
         
         
