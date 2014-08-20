#Vectors
#4/21/2014
#Sydney Simpson

import math

def make_vector(vector1):
    vector_1= vector1.split(" ")
    vector=[]
    for num in vector_1:
        new_num=eval(num)
        vector.append(new_num)
    return vector

def add_vectors(A,B):
    vector_combine=[]
    for values in range(len(A)):
        vector_combine.append(A[values]+B[values])
    return vector_combine

def dot_product(A,B):
    vector_dot=[]
    for values in range(len(A)):
        vector_dot.append(A[values]*B[values])
    new_vector=0
    for num in vector_dot:
        new_vector+=num
    return new_vector

def vector_norm(vector):
    norm=0
    for value in vector:
        norm+=value**2
    norm=math.sqrt(norm)
    norm=round(norm,2)
    return norm
    

vector_1=input("Enter vector A:\n")
vector_a=make_vector(vector_1)

vector_2=input("Enter vector B:\n")
vector_b=make_vector(vector_2)

print("A+B =", add_vectors(vector_a,vector_b))

print("A.B =", dot_product(vector_a,vector_b))

print("|A| = {0:.2f}".format(vector_norm(vector_a)))
print("|B| = {0:.2f}".format(vector_norm(vector_b)))