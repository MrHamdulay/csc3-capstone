"""Addition, dot product and normalization of vectors
Carla Wilby
19 April 2014"""

import math

#get and store vectors to arrays
vectorA = input("Enter vector A:\n")
vectorB = input("Enter vector B:\n")
vector_arrayA = vectorA.split(" ")
vector_arrayB = vectorB.split(" ")

#addition of vectors
vector_add = []
for i in range(3):
    vector_add.append(eval(vector_arrayA[i])+eval(vector_arrayB[i]))
print("A+B =",vector_add)

#dot product of vectors
dot_prod = 0
for i in range(3):
    dot_prod += eval(vector_arrayA[i])*eval(vector_arrayB[i])
print("A.B =", dot_prod)

#normalization of vectors
A = 0
B = 0
for i in range(3):
    A += eval("("+vector_arrayA[i]+")")**2
print("|A| =","{0:.2f}".format(math.sqrt(A)))
for i in range(3):
    B += eval("("+vector_arrayB[i]+")")**2
print("|B| =","{0:.2f}".format(math.sqrt(B)))
