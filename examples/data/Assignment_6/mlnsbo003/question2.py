'''Vectors Program
Sbongakonke Mlangeni
20 April 2014'''

from math import sqrt

#taking vector components
x = input('Enter vector A:\n')
y = input('Enter vector B:\n')

#creating lists respectively
A = x.split(' ')
B = y.split(' ')

Areal = []
Breal = []

#for i in A:
#    a = eval(i)
#    Areal.append(a)
    
#for i in B:
#    a = eval(i)
#    Breal.append(a)

#vector addition    
AplusB = []
for i in range(3):
    AplusBcomp = int(A[i])+int(B[i])
    AplusB.append(AplusBcomp)
    
print('A+B =',AplusB)

#dot product
AbyB=0
for i in range(3):
    AbyBcomp = int(A[i])*int(B[i])
    AbyB += AbyBcomp

print('A.B =',AbyB)

#normalization
absA = 0
absB = 0
for i in range(3):
    AcompSqd = (int(A[i]))**2
    absA += AcompSqd
absA = sqrt(absA)
print('|A| = {0:.2f}'.format(absA))

for i in range(3):
    BcompSqd = (int(B[i]))**2
    absB += BcompSqd
absB = sqrt(absB)
print('|B| = {0:.2f}'.format(absB))

#zero case
def ZeroCase():
    if x == '0 0 0' and y == '0 0 0':
        print('A+B = [0, 0, 0]')
        print('A.B = 0')
        print('|A| = 0.00')
        print('|B| = 0.00')

