"""Daniel Schwartz
SCHDAN037
question 2
april 2014"""

import math


def sum_of_vectors(a, b):
    """ adds the vectors a and b together and returns the list of the
    new vector"""

    sum_vector = [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
    return sum_vector


def mult_of_vectors(a, b):
    """multiplies the vectors a and b and returns the values"""
    mult_vector = 0

    for i in range(len(a)):
        mult_vector += (a[i] * b[i])

    return mult_vector


def norm_of_vector(a):
    """ normalizes a vector and returns the values"""

    norm_vector = math.sqrt((a[0]**2) + (a[1]**2) + (a[2]**2))
    norm_vector = round(norm_vector, 2)

    return norm_vector


def main():
    """main"""
    # initial variables
    vect_A = []
    vect_B = []

    # entering vectors
    vect_A = input("Enter vector A:\n").split(" ")
    vect_B = input("Enter vector B:\n").split(" ")

    # make values into workable integers instead of strings
    for i in range(len(vect_A)):
        vect_A[i] = int(vect_A[i])

    for i in range(len(vect_B)):
        vect_B[i] = int(vect_B[i])

    # sum of vectors
    vect_sum = sum_of_vectors(vect_A, vect_B)
    print("A+B = " + str(vect_sum))

    # dot multiplication of vectors
    vect_mult = mult_of_vectors(vect_A, vect_B)
    print("A.B = " + str(vect_mult))

    # normalization of vectors
    vect_A_norm = norm_of_vector(vect_A)
    vect_B_norm = norm_of_vector(vect_B)

    if vect_A_norm == 0.00:
        print("|A| = 0.00")
    else:
        print("|A| = " + str(vect_A_norm))

    if vect_B_norm == 0.00:
        print("|B| = 0.00")
    else:
        print("|B| = " + str(vect_B_norm))


#runs main on entry
if __name__ == '__main__':
    main()