#shaylan lalloo
#Does vector operations

from math import *

a = list(map(int, input('Enter vector A:\n').split()))
#read inputs

b = list(map(int, input('Enter vector B:\n').split()))
#read inputs

print('A+B =', [a[0] + b[0], a[1] + b[1], a[2] + b[2]])
#output sum

print('A.B =', a[0]*b[0] + a[1]*b[1] + a[2]*b[2])
#output dot product

print('|A| =', "{0:.2f}".format(round(sqrt(a[0]**2 + a[1]**2 + a[2]**2), 2)))
#output size of a

print('|B| =', "{0:.2f}".format(round(sqrt(b[0]**2 + b[1]**2 + b[2]**2), 2)))
#output size of b
