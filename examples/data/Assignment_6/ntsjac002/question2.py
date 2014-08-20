'''A program that takes to vectors from the user and do dot product,vector addition and vector normalisation
Jacob Ntesang
21 April 2014'''

from math import*

#Ask the user for the input of two vectors
V_A = input("Enter vector A:\n")
V_B = input("Enter vector B:\n")


V_A = V_A.split()
V_B = V_B.split()
#creat a list of vectors
V_AB = []
V_DOT = 0
V_MAGN_A = 0
V_MAGN_B = 0


for i in range(len(V_A)):
    V_AB.append(int(V_A[i])+int(V_B[i]))
    V_DOT += (int(V_A[i])*int(V_B[i]))
    V_MAGN_A += (int(V_A[i])**2)
    V_MAGN_B += (int(V_B[i])**2)
    
print("A+B = ", V_AB,sep="")
print("A.B = ", V_DOT,sep="")
print("|A| = ", "%.2f"%round((sqrt(V_MAGN_A)),2),sep="")
print("|B| = ", "%.2f"%round((sqrt(V_MAGN_B)),2),sep="")