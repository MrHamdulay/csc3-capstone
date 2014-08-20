# Student Number: PRTNIC017
# Date: 4/22/14

from math import *

a = eval('[' + input('Enter vector A:\n').replace(' ', ',') + ']')
b = eval('[' + input('Enter vector B:\n').replace(' ', ',') + ']')

# ADDITION
plus = [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
print('A+B =', plus)

# DOT PRODUCT
dot = (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])
print('A.B =', dot)

# A and B
absa = abs(sqrt((a[0] ** 2) + (a[1] ** 2) + (a[2] ** 2)))
absb = abs(sqrt((b[0] ** 2) + (b[1] ** 2) + (b[2] ** 2)))
print('|A| =', "{:.2f}".format(absa))
print('|B| =', "{:.2f}".format(absb))