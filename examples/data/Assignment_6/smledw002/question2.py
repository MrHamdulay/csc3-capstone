#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 20 April 2014
#Function       : adds multiplies and normalises vectors
#Title          : Question2

from math import *


def vector_add(vectora, vectorb):

    """Returns the sum of two vectors in the form of a list"""

    vector_sum = []
    for i in range(3):
        #adds the the sum of each component to a new list
        vector_sum.append(vectora[i] + vectorb[i])

    return vector_sum


def vector_multiplier(vectora, vectorb):

    """Returns the dot product of two vectors in the form of a list """

    vector_multiplied = []
    for i in range(3):
        #adds the the product of each component to a new list
        vector_multiplied.append(vectora[i] * vectorb[i])

    return sum(vector_multiplied)


def vector_normalization(vector):

    """Determines the norm of a vector"""

    sum_squared = 0
    index_no = 0

    for i in range(3):
        sum_squared += (vector[index_no]) ** 2
        index_no += 1
    return "{0:.2f}".format(sqrt(sum_squared))

#Gets a vector in the form of a list of digits

vector_A = list(map(eval, (input("Enter vector A:\n").split())))

vector_B = list(map(eval, (input("Enter vector B:\n").split())))

print("A+B =", vector_add(vector_A, vector_B))
print("A.B =", vector_multiplier(vector_A, vector_B))
print("|A| =", vector_normalization(vector_A))
print("|B| =", vector_normalization(vector_B))








