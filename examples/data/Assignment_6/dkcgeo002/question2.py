__author__ = 'George de Kock'
""" Basic Vector Calculations
    2014-4-20   """

import math
A = input("Enter vector A:\n").split(" ")
B = input("Enter vector B:\n").split(" ")
sumAB = []
dot = 0
sumA, sumB = 0, 0
for x in range(len(A)):
    sumAB.append(int(A[x])+int(B[x]))
    dot += (int(A[x])*int(B[x]))
    sumA += int(A[x])**2
    sumB += int(B[x])**2
print("A+B =",sumAB)
print("A.B =",dot)
if (sumA == 0) and (sumB == 0):
    print("|A| = 0.00")
    print("|B| = 0.00")
else:
    print("|A| =",str(round(math.sqrt(sumA), 2)))
    print("|B| =",str(round(math.sqrt(sumB), 2)))