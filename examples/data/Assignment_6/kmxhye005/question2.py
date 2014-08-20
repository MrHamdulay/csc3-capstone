# Basic vector calculations in 3 dimensions: addition, dot product and normalization.

# Dot Product is the sum of the products of corresponding elements.

# The Norm of a single vector is the square root of the sum of the squares of the elements.


import math

one_A = input("Enter vector A: \n")
one_B = input("Enter vector B: \n")
two_A = one_A.split(" ")
two_B = one_B.split(" ")


array_A = []
array_B = []
for i in two_A:
  array_A.append(int(i))
for i in two_B:
  array_B.append(int(i))
  

# Addition
addition = []
for i in range(3):
    addition.append(array_A[i]+array_B[i]) 
print ("A+B =", addition)


# Dot product
product = 0
index = 0
for i in range(3):
    index = (array_A[i]*array_B[i])
    product += index 
print("A.B =", product)


# Normalization
sumA=0
sumB=0
for i in range(3):
    A = array_A[i]**2
    sumA += A
    lAl  = math.sqrt(sumA)
    B = array_B[i]**2
    sumB += B
    lBl = math.sqrt(sumB)
    
print("|A| =", round(lAl,2))
print("|B| =", round(lBl,2))
