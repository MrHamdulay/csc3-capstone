#A program that does basic vector calculations in 3 dimensions
#Author: Emiel Zyde
#Date: 20 April 2014

import math   #we will be using various mathematical functions 

#get vectors from user and convert them into a list
vector_A = input("Enter vector A:\n")
vector_B = input("Enter vector B:\n")
vector_A = vector_A.split()
vector_B = vector_B.split()

#create a function for vector addition
def vector_addition(vector1, vector2):
    vector_add = []
    for i in range(3):
        sum_vectors = int(vector1[i]) + int(vector2[i])
        vector_add.append(sum_vectors)
        
    print("A+B =", vector_add)
    
#create a function for dot product 
def dot_product(vector1, vector2):
    product = 0
    for i in range(3):
        product_vectors = int(vector1[i]) * int(vector2[i])
        product = product + product_vectors
    
    print("A.B =", product)
    
#create a function to find the norm of vector A:
def norm_A(vector_A):
    norm = 0
    for i in range(3):
        square = int(vector_A[i])**2
        norm = norm + square
    norm = math.sqrt(norm)
    norm = "{0:.2f}".format(norm)  #this formatting structure allows us to overcome an error where automatic marker expected an output of 0.00 at one stage and the other version of the program (using round(...,2)) only gave 0.0
    
    print("|A| =", norm)

#create a function to find the norm of vector B:
def norm_B(vector_B):
    norm = 0
    for i in range(3):
        square = int(vector_B[i])**2
        norm = norm + square
    norm = math.sqrt(norm)
    norm = "{0:.2f}".format(norm)
    
    print("|B| =", norm)

vector_addition(vector_A, vector_B)
dot_product(vector_A, vector_B)
norm_A(vector_A)
norm_B(vector_B)