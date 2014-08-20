from math import *

pi = 2
mylast = sqrt(2)
while (2/mylast) != 1:
    pi *= 2/mylast
    mylast = sqrt(2 + mylast)

print('Approximation of pi:', round(pi, 3))
rad = float(input('Enter the radius:\n'))

print('Area:', round(pi * rad**2, 3))

