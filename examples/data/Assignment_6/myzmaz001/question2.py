""" Program to do basic vector calculations in 3 dimensions
Mazwi Myeza
21 April 2014
Assignment6
Question2
"""
import math
#Getting vector information from user and creating arrays
a = input("Enter vector A:\n")
A = a.split(" ")
b = input("Enter vector B:\n")
B = b.split(" ")
vecA = []
vecB = []
vecAB = []
vecAdotB = []
#Adding information to arrays
for i in range(3):
    vecA.append(eval(A[i]))
    vecB.append(eval(B[i]))
    vecAB.append(vecA[i]+vecB[i])
    vecAdotB.append(vecA[i]*vecB[i])
#printing results
print("A+B =", vecAB)
print("A.B =",vecAdotB[0]+vecAdotB[1]+vecAdotB[2])
print("|A| =",'{0:0.2f}'.format(math.sqrt((vecA[0]**2)+(vecA[1]**2)+(vecA[2]**2))))
print("|B| =",'{0:0.2f}'.format(math.sqrt((vecB[0]**2)+(vecB[1]**2)+(vecB[2]**2))))    

    