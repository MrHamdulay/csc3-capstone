"""ASsignment 6 Question 2 basic vector calculations in 3-d
joshua wort
19 april 2014"""

import math

#get list of vector A 
a=input("Enter vector A:\n")
vectorA = a.split(" ")

#get list of vector B
b=input("Enter vector B:\n")
vectorB = b.split(" ")

#sum of vector A and vector B
sum_vectors=[]
for i in range(3):
    s=int(vectorA[i]) + int(vectorB[i])
    sum_vectors.append(s)
print("A+B =",sum_vectors)

#product of vector A and vector B
dot_product=0
for j in range(3):
    product=int(vectorA[j])*int(vectorB[j])
    dot_product+=product
print("A.B =",dot_product)

#get normA
normA=0
for k in range(3):
    A=int(vectorA[k])**2
    normA+=A
normA=math.sqrt(normA)
normA="{0:.2f}".format(normA)
print("|A| =",normA)

#get normB
normB=0
for l in range(3):
    B=int(vectorB[l])**2
    normB+=B
normB=math.sqrt(normB)
normB="{0:.2f}".format(normB)
print("|B| =",normB)