#kereshnee pillay
# 21 april
# maths calculations

import math

#Enter and store vectors in a list
A = input("Enter vector A:\n").split(" ")

B = input("Enter vector B:\n").split(" ")

#Converting string elements in arrays to integers for easier calculations
for i in range (len(A)):
    A[i] = eval(A[i])
    B[i] = eval(B[i])
  

#Addition
sum_vectors = []
for i in range(len(A)):
    sum_vectors.append(A[i] + B[i]) #Appending sums to new array sum_vectors
    
    
#Dot product
dot_product = 0
for i in range(len(sum_vectors)):\
    dot_product += (A[i] * B[i])


norm_A = 0
norm_B = 0

#Normalisation of A
for a in A:
    norm_A += a**2 #Sum of squares
norm_A = math.sqrt(norm_A)#Square root of sum of squares
    
    
#Normalisation of B
for b in B:
    norm_B += b**2 #Sum of squares
norm_B = math.sqrt(norm_B)#Square root of sum of squares


#Print 
print("A+B =", sum_vectors)
print("A.B =", dot_product)
print("|A| =", "{:.2f}".format(norm_A, 3))
print("|B| =", "{:.2f}".format(norm_B, 3))



