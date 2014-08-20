import math

A = input('Enter vector A:\n')
B = input('Enter vector B:\n')

arrA = []
arrA = A.split(" ")

arrB = []
arrB = B.split(" ")

arrC = []

for k in range(0, 3):
    p = eval(arrA[k]) + eval(arrB[k])
    arrC.append(p)
    
print('A+B =', arrC)



plus = 0
m = 0

for k in range(0, 3):
    m = eval(arrA[k]) * eval(arrB[k])
    plus += m
    
print('A.B =', plus)



sumA = 0
for k in range(0, 3):
    sumA += eval(arrA[k])**2
        
ansA = math.sqrt(sumA)

outA = "{0:.2f}".format(ansA)

print('|A| =', outA)



sumB = 0
for k in range(0, 3):
    sumB += eval(arrB[k])**2
        
ansB = math.sqrt(sumB)

outB = "{0:.2f}".format(ansB)

print('|B| =', outB)