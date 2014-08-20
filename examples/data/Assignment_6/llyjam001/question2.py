"""Assignment 6 Question 2
James Lloyd
21 April 2014"""

A_plus_B=[]
A=[]
B=[]
import math

#Getting A and B

strA=input("Enter vector A:\n")
A=strA.split(" ")

for i in range(len(A)):
    A[i]=eval(A[i])

strB=input("Enter vector B:\n")
B=strB.split(" ")

for i in range(len(B)):
    B[i]=eval(B[i])

#Vector Addition
for i in range(0,3):
    addition=A[i]+B[i]
    A_plus_B.append(addition)
    
#Scalar Dot Product
dot_product=(A[0]*B[0])+(A[1]*B[1])+(A[2]*B[2])

#Magntitude of A and B
sumA=0
sumB=0
for i in range(0,3):
    sumA+=(A[i])**2
    sumB+=(B[i])**2
    
mag_A=math.sqrt(sumA)
mag_B=math.sqrt(sumB)


#rounding to two decimal places
mag_A=round(mag_A,2)
mag_B=round(mag_B,2)
if mag_A==0.0:
    mag_A="0.00"
if mag_B==0.0:
    mag_B="0.00"

    
#Printing

print("A+B =",A_plus_B)
print("A.B =",dot_product)
print("|A| =",mag_A)
print("|B| =",mag_B)
