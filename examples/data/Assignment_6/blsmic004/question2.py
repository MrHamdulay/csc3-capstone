'''program to do basic vector calculations in 3 dimensions: addition, dot product and normalization
Michele Balestra  BLSMIC004
23 April 2014'''

import math

# gets values for each vector from user
vectorA = (input("Enter vector A:\n")).split()
vectorB = (input("Enter vector B:\n")).split()

# calculates and prints the addition of vectors
addition = []
for i in range(3):
    addition.append(eval(vectorA[i]) + eval(vectorB[i]))
print("A+B =", addition)

# calculates and prints the product of vectors
product = 0
for j in range(3):
    product += (eval(vectorA[j]) * eval(vectorB[j]))
print("A.B =", product)

# calculates and prints to normalisation of vector A
normalA = 0
for k in range(3):
    normalA += eval(vectorA[k])**2
if math.sqrt(normalA)==0.0:
    print("|A| = 0.00")
else:
    print("|A| =", round(math.sqrt(normalA),2))

# calculates and prints to normalisation of vector B
normalB = 0
for l in range(3):
    normalB += eval(vectorB[l])**2
if math.sqrt(normalB)==0.0:
    print("|B| = 0.00")
else:
    print("|B| =", round(math.sqrt(normalB),2))