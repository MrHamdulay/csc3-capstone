'''3D vector calculations
Frans Ledwaba
24 April 2014'''

import math
 
#get vectors    
a = input('Enter vector A:\n')
b = input('Enter vector B:\n')

#put vectors in a list
A = a.split( )
B = b.split( )

#evalute vectors
for i in range(len(A)):
    A[i] = eval(A[i])
    B[i] = eval(B[i])

#adding vectors
c = [] #new list
for x in range(len(A)):
    d = A[x] + B[x]
    c.append(d)
print('A+B =', c)

#multiply vectors
e = [] #new list
for y in range(len(A)):
    f = A[y] * B[y]
    e.append(f)
e = e[0]+e[1]+e[2]
print('A.B =', e)

#absolute value of A
g = 0
for z in range(len(A)):
    h = (A[z])**2
    g = g + h
if g == 0:
    print('|A| =', "0.00")
else:
    g = round(math.sqrt(g), 2)
    print('|A| =', g)

#absolue value of B
j = 0
for w in range(len(B)):
    k = (B[w])**2
    j = j + k
if j == 0:
    print('|B| =', "0.00")
else:
    j = round(math.sqrt(j), 2)
    print('|B| =', j)