

import math


A = input("Enter vector A:\n").split(" ")

B = input("Enter vector B:\n").split(" ")


for i in range (len(A)):
    A[i] = eval(A[i])
    B[i] = eval(B[i])

sum_vectors = []
for i in range(len(A)):
    sum_vectors.append(A[i] + B[i]) 
    
    

product = 0
for i in range(len(sum_vectors)):\
    product += (A[i] * B[i])


norm_A = 0
norm_B = 0
 
 
for a in A:
    norm_A += a**2 
norm_A = math.sqrt(norm_A)
    

for b in B:
    norm_B += b**2  
norm_B = math.sqrt(norm_B)


#ouput
print("A+B =", sum_vectors)
print("A.B =", product)
print("|A| =", "{:.2f}".format(norm_A, 3))
print("|B| =", "{:.2f}".format(norm_B, 3))



