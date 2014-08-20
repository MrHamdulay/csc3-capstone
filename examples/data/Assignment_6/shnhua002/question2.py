#Charlie Shang
#SHNHUA002
#Assignment 6 Q2

import math

A = input("Enter vector A:\n").split(" ")
B = input("Enter vector B:\n").split(" ")

for i in range(0,3,1): #convert vector to integers from string
    A[i]=int(A[i])
    B[i]=int(B[i])

print("A+B = [",A[0] + B[0], ", " , A[1] + B[1], ", ", A[2] + B[2], "]", sep='') #addition

print("A.B =",(A[0]*B[0]) + (A[1]*B[1]) + (A[2]*B[2])) #dot product

SqrtA = math.sqrt((A[0]**2) + (A[1]**2) + (A[2]**2)) #normalisation
SqrtB = math.sqrt((B[0]**2) + (B[1]**2) + (B[2]**2))

print("|A| = %0.2f" % round(SqrtA,2)) #round to 2 decimals
print("|B| = %0.2f" % round(SqrtB,2))