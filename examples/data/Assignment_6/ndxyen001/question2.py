# Yentl Naidu (NDXYEN001)
# 23 April 2014
# Assignment 6
# Question 2

import math

# Create empty lists
A = []
B = []

# Input for the vector values
vector_a = (input("Enter vector A:\n"))
vector_b = (input("Enter vector B:\n"))

# Separates string into a list
vector_a = str(vector_a)
A = vector_a.split(" ") 
# print(A) just to test

vector_b = str(vector_b)
B = vector_b.split(" ")
# print(B) just to test


# Calculations:
# Addition of vectors
add = (int(A[0]))+(int(B[0])) 
add_1 = (int(A[1]))+(int(B[1])) 
add_2 = (int(A[2]))+(int(B[2]))

# Dot products
dot = (int(A[0]))*(int(B[0]))
dot_1 = (int(A[1]))*(int(B[1]))
dot_2 = (int(A[2]))*(int(B[2]))
dot_product = dot + dot_1 + dot_2

# Norm
norm_A_0 = (int(A[0]))**2
norm_A_1 = (int(A[1]))**2
norm_A_2 = (int(A[2]))**2
norm_A = (norm_A_0+norm_A_1+norm_A_2)
norm_A = math.sqrt(norm_A)

norm_B_0 = (int(B[0]))**2
norm_B_1 = (int(B[1]))**2
norm_B_2 = (int(B[2]))**2
norm_B = (norm_B_0+norm_B_1+norm_B_2)
norm_B = math.sqrt(norm_B)

# Printing the results
print("A+B =", [add,add_1,add_2])
print("A.B =", dot_product)
print("|A| = {0:.2f}".format(norm_A))
print("|B| = {0:.2f}".format(norm_B))