# Student Number: PRTNIC017
# Date: 3/7/14

import math

# HAS SOME PIES, MUCH PIES
pie = 2
term = 2 ** 0.5
while 2 / term > 1:
    pie *= (2 / term)
    term = math.sqrt(2 + term)

# PRINT
print('Approximation of pi:', round(pie,3))
radius = eval(input('Enter the radius:\n'))
area = pie * (radius ** 2)
print('Area:', round(area, 3))