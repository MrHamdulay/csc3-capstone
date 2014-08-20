#Code to do basic vector calculations in 3 dimensions: addition, dot product and normalization. 
#Saul Bloch
#22 April 2014

import math
#inputting vector values
firstThree = input("Enter vector A:\n")

secondThree = input("Enter vector B:\n")
#creating arrays
C = [0,0,0]
D = [0,0,0]
E = [0,0,0]
F = [0,0,0]
#creating new arrays
A = firstThree.split(" ")
B = secondThree.split(" ")
#adding arrays (vectors)
C[0] = int(A[0])+int(B[0])
C[1] = int(A[1])+int(B[1])
C[2] = int(A[2])+int(B[2])
#multiplying arrays (vectors)
D[0] = int(A[0])*int(B[0])
D[1] = int(A[1])*int(B[1])
D[2] = int(A[2])*int(B[2])
#squaering arrays (vectors)
E[0] = int(A[0])*int(A[0])
E[1] = int(A[1])*int(A[1])
E[2] = int(A[2])*int(A[2])
#squaering arrays (vectors)
F[0] = int(B[0])*int(B[0])
F[1] = int(B[1])*int(B[1])
F[2] = int(B[2])*int(B[2])

#printing vectors
print("A+B = ",end="") 
print(C)
print("A.B =",D[0]+D[1]+D[2])
print("|A| = ",end = "")
print("%.2f" % round(math.sqrt(E[0]+E[1]+E[2]),2))
print("|B| = ",end = "")
print("%.2f" % round(math.sqrt(F[0]+F[1]+F[2]),2))



