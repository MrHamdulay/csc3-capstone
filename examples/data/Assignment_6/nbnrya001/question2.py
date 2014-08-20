from math import *

f = lambda x : int(x)

a = input('Enter vector A:\n').split()
for i in range(len(a)): a[i] = f(a[i])

b = input('Enter vector B:\n').split()
for i in range(len(b)): b[i] = f(b[i])

g = lambda x, y : x + y
h = lambda x, y : x * y

abplus = []
for i in range(3):
    abplus.append(g(a[i], b[i]))

print('A+B =', abplus)

abtimes = 0
for i in range(3):
    abtimes += (h(a[i], b[i]))

print('A.B =', abtimes)

m = lambda x : x**2
n = lambda x : '{0:.2f}'.format(round(sqrt(m(x[0]) + m(x[1]) + m(x[2])), 2))

print('|A| =', n(a))
print('|B| =', n(b))
