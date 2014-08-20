import math
pi =2
denom = math.sqrt(2)
while denom != 2:
  pi = pi*2/denom
  denom = math.sqrt(2+denom)
  
print('Approximation of pi:',round(pi,3),sep=' ')
radius = eval(input('Enter the radius:\n'))
area = pi*radius**2
print('Area:', round(area,3))