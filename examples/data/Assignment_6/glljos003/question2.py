"""program to do vector calculations in 3 dimensions
joshua gullan
22 april 2014"""

from math import *

#get values, split them and evaluate to create lists A and B
A=list(map(eval, input("Enter vector A:\n").split()))
B=list(map(eval, input("Enter vector B:\n").split()))

#adding vector A and B using indexes
AAA=[A[0]+B[0], A[1]+B[1], A[2]+B[2]]
print("A+B =", AAA)

#adding vectors and adding the remaining 3 values to form answer
C=[A[0]*B[0], A[1]*B[1], A[2]*B[2]]
print("A.B =", C[0]+C[1]+C[2])

#squaring each value in vector A
AA=[A[0]**2, A[1]**2, A[2]**2]

#adding the squares and getting the square root of the sum
AB=sqrt(AA[0]+AA[1]+AA[2])

#if the answer is 0, prints 0.0 else rounds off answers to two decimals
if AB==0:
    print("|A| = 0.00")
elif AB!=0:
    print("|A| =", "{0:0.2f}".format(AB))

#does same as above but for B     
BB=[B[0]**2, B[1]**2, B[2]**2]
BA=sqrt(BB[0]+BB[1]+BB[2])

#if the answer is 0, prints 0.0 else rounds off answers to two decimals
if BA==0:
    print("|B| = 0.00")
elif BA!=0:
    print("|B| =", "{0:0.2f}".format(BA))


