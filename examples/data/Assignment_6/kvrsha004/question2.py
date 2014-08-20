""" Q2 of Assignment 6: Vector Calculations
 KVRSHA004
 20th April 2014 """

A = input("Enter vector A: \n")
B = input("Enter vector B: \n")
vecA = A.split(" ")
vecB = B.split(" ")

#Vector addition
AplusB = []
for i in range(3):
    x = eval(vecA[i]) + eval(vecB[i])
    AplusB.append(x)
print("A+B =", AplusB)

#Dot product
AdotB = 0
for i in range(3):
    x = eval(vecA[i]) * eval(vecB[i])
    AdotB += x
print("A.B =", AdotB)

#Normalisations
normA = 0
normB = 0
for i in range(3):
    normA += eval(vecA[i]) ** 2
    normB += eval(vecB[i]) ** 2
normA, normB = "{0:0.2f}".format(normA**0.5), "{0:0.2f}".format(normB**0.5, 2)
print("|A| =", normA)
print("|B| =", normB)