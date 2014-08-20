"""program to do basic vector calculations
Kristin Kinmont
20 April 2014"""

import math

#get vectors
a = input("Enter vector A:\n")
b = input("Enter vector B:\n")

#create 2 lists
A = a.split(" ")
B = b.split(" ")

#addition
addition = []
for i in range(3):
    variable = eval(A[i])+eval(B[i])
    addition.append(variable)
print("A+B =",addition)

#dot product
dot = 0
for i in range(3):
    dot += eval(A[i])*eval(B[i])
print("A.B =",dot)
    
#normalization for A
normalA = 0
for i in range(3):
    normalA += eval(A[i])**2
normalA = math.sqrt(normalA)
normalA ='{0:.2f}'.format(normalA)
print("|A| =",normalA)

#normalization for B
normalB = 0
for i in range(3):
    normalB += eval(B[i])**2
normalB = math.sqrt(normalB)
normalB ='{0:.2f}'.format(normalB)
print("|B| =",normalB)

