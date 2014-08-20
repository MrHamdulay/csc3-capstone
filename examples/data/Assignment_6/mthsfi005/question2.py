'''a program to do basic vecor calculations in 3D
Sfiso Mthembu MTHSFI005
04/20/2014'''

import math
#for vector A

vector_A=[]

vector_a=input("Enter vector A:\n")

vector_a=vector_a.split(" ")

for i in vector_a:
    vector_A.append(eval(i))

#for vector B

vector_B=[]

vector_b=input("Enter vector B:\n")

vector_b=vector_b.split(" ")

for i in vector_b:
    vector_B.append(eval(i))
    
#for vector addition
vector_addition=[vector_A[0] + vector_B[0] , vector_A[1] + vector_B[1] , vector_A[2] + vector_B[2]]

#for vector multiplication
dot_product = (vector_A[0] * vector_B[0]) + (vector_A[1] * vector_B[1]) + (vector_A[2] * vector_B[2])

from math import sqrt

#for size of A
magnitude_A = sqrt((vector_A[0]*vector_A[0]) + (vector_A[1]*vector_A[1]) + vector_A[2]*vector_A[2])

#for size of B
magnitude_B = sqrt((vector_B[0]*vector_B[0]) + (vector_B[1]*vector_B[1]) + (vector_B[2]*vector_B[2]))

print("A+B =" , vector_addition)
print("A.B =" , dot_product)
print("|A| =" ,"{0:.2f}".format(magnitude_A,2))
print("|B| =" , "{0:.2f}".format(magnitude_B,2))