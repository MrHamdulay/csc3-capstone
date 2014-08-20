"""a program to do basic vector calculations in 3 dimensions
fadzai mupfunya
21/04/14"""
import math
#splitting the nunbers entered by user into individual strings
vectorA=input("Enter vector A:\n")
vectorB=input("Enter vector B:\n")
A=vectorA.split(" ")
B=vectorB.split(" ")

#for vector addition
add1=int(A[0]) + int(B[0])
add2=int(A[1]) + int(B[1])
add3=int(A[2]) + int(B[2]) 
addition=[add1,add2,add3]
print("A+B =",addition)


#for vector dot product
mult1=int(A[0]) * int(B[0])
mult2=int(A[1]) * int(B[1])
mult3=int(A[2]) * int(B[2])
dot_product=(mult1+mult2+mult3)
print("A.B =",dot_product)

#for the norm of a vector A
A_squared=((int(A[0])**2) + (int(A[1])**2) + (int(A[2])**2))
normA=round(math.sqrt(A_squared),2)

if A_squared==0:
    print("|A| = 0.00")
else:
    print("|A| =",normA)


#for the norm of a vector B
B_squared=((int(B[0])**2) + (int(B[1])**2) + (int(B[2])**2))
normB=round(math.sqrt(B_squared),2)
if B_squared==0:
    print("|B| = 0.00")
else:
    print("|B| =",normB)