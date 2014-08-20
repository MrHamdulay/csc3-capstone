import math
pi = 2
volgende = math.sqrt(2)
while (2/volgende) != 1:
    pi *= 2/volgende
    volgende = math.sqrt(2+volgende)
print('Approximation of pi:',round(pi,3))
radius = eval(input('Enter the radius:\n'))
area = pi*(radius**2)
print('Area:', round(area,3))