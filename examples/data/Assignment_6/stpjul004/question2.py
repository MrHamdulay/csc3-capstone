""" Program that performs vector calculations
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-04-23 """

import math

#recieve two vectors
vector_a = input("Enter vector A:\n").split(" ")
vector_b = input("Enter vector B:\n").split(" ")

#convert into a list of ints
for i in range(3):
    vector_a[i] = int(vector_a[i])
    vector_b[i] = int(vector_b[i])

#Add the vectors together
def add_vectors(vecta, vectb):
    new_vect = []
    for i in range(3):
        new_vect.append(vecta[i] + vectb[i])
    return new_vect

#Find the dot product of the vectors
def dot_product(vecta, vectb):
    product = 0
    for i in range(3):
        product += vecta[i]*vectb[i]
    return product

#Find the magnitude of a vector
def mag_vector(vector):
    magnitude = 0
    for i in range(3):
        magnitude += vector[i]**2
    return math.sqrt(magnitude)

print("A+B =",add_vectors(vector_a, vector_b))
print("A.B =",dot_product(vector_a, vector_b))
print("|A| = {:.2f}".format(mag_vector(vector_a)))
print("|B| = {:.2f}".format(mag_vector(vector_b)))