# Assignment 6 question 2
# Amy Brodie
# 24/04/2014

import math

A = input("Enter vector A:\n") 
B = input("Enter vector B:\n") 
vectorA = []
vectorB = []
addition = []
AB = 0

# Assign vectors to lists
for i in range(3):
    posA = A.find(" ")
    posB = B.find(" ")
    if posA == -1:
        vectorA.append(eval(A))
    else:
        vectorA.append(eval(A[:posA]))
        A = A[posA+1:]
    if posB == -1:
        vectorB.append(eval(B))
    else:
        vectorB.append(eval(B[:posB]))
        B = B[posB+1:]

# A+B
for i in range(3):
    addition.append(vectorA[i] + vectorB[i])
    
# A.B
for i in range(3):
    AB += vectorA[i]*vectorB[i]
    
# |A|
A_norm = math.sqrt(vectorA[0]**2+vectorA[1]**2+vectorA[2]**2)

# |B|
B_norm = math.sqrt(vectorB[0]**2+vectorB[1]**2+vectorB[2]**2)

# output
print("A+B =", addition)
print("A.B =", AB)
print("|A| =", "{0:.2f}".format(A_norm))
print("|B| =", "{0:.2f}".format(B_norm))