# 24 April 2014
# Shaun Muzenda
# Doing basic calculations using vectors inputed by the user

import math

vector_A = input("Enter vector A:\n")   #user inputing vector A
A = vector_A.split()

vector_B = input("Enter vector B:\n")   #user inputing vector B
B = vector_B.split()

sum_of_vectors = [int(A[0])+int(B[0]),int(A[1])+int(B[1]),int(A[2])+int(B[2])]  #calculating the addition of the two vectors
print("A+B =",sum_of_vectors)

dot_product_of_vectors = int(A[0])*int(B[0])+int(A[1])*int(B[1])+int(A[2])*int(B[2])    #calculatig the the dot product of the two vectors
print("A.B =",dot_product_of_vectors)


modulus_of_A = math.sqrt(int(A[0])**2 +int(A[1])**2 +int(A[2])**2)  #calculating the modulus of vector A
print("|A| =","{0:.2f}".format(modulus_of_A))  #returns the answer to 2 decomal points


modulus_of_B = math.sqrt(int(B[0])**2 +int(B[1])**2 +int(B[2])**2)  #calculating the modulus of vector B
print("|B| =","{0:.2f}".format(modulus_of_B))   #returns the answer to 2 decomal points


