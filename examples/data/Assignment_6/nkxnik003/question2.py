#ComSci Assignment 6
#Nikhil Jiten Naik
#25/04/2014
#Question 2

from math import *

A=input("Enter vector A:\n")
B=input("Enter vector B:\n")

A=A.split(" ")
A1=eval(A[0])
A2=eval(A[1])
A3=eval(A[2])
B=B.split(" ")
B1=eval(B[0])
B2=eval(B[1])
B3=eval(B[2])

AdotB=(A1 * B1) + (A2 * B2) + (A3 * B3)

if (A1**2+A2**2+A3**2) == 0:
    normA="0.00"
else:
    normA=round(sqrt(A1**2+A2**2+A3**2), 2)
if (B1**2+B2**2+B3**2) == 0:
    normB="0.00"
else:
    normB=round(sqrt(B1**2+B2**2+B3**2), 2)

print("A+B = [",A1+B1,", ",A2+B2,", ",A3+B3,sep="",end="]\n")

print("A.B =",AdotB)
print("|A| =",normA)
print("|B| =",normB)
