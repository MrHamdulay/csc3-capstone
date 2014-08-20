# Program to to basic vector calculations
# Dalise Steynfaard
# STYDAL001
# 26 April 2014

import math

def addVec(a, b):
    """Calculates and returns the sum of vectors a and b"""
    sum_vector = []
    for i in range(len(a)):
        # Calculates the sum of every index and adds it to the new vector
        sum_vector.append(eval(a[i]) + eval(b[i]))
    
    return sum_vector

def prodVec(a,b):
    """Calculates and returns the product of vectors a and b"""
    prod_value = 0
    
    for i in range(len(a)):
        # Calculates the product of every index and adds it to the new vector
        prod_value += (eval(a[i]) * eval(b[i]))
    
    return prod_value

def absVec(a):
    """Calculates and returns the absolute value of a vector"""
    abs_value = 0.0
    
    for i in range(len(a)):
        # Calculates the absolute value of vector a
        abs_value += eval(a[i])**2
    
    abs_value = round(math.sqrt(abs_value), 2)
    
    return abs_value

def main():
    """Gets vector a and b from user and prints answers to basic vector calculations"""
    vec_A = input("Enter vector A:\n").split(' ')
    vec_B = input("Enter vector B:\n").split(' ')
    
    abs_vec_A = "{:.2f}".format(absVec(vec_A))
    abs_vec_B = "{:.2f}".format(absVec(vec_B))
    
    print("A+B =", addVec(vec_A, vec_B))
    print("A.B =", prodVec(vec_A, vec_B))
    print("|A| =", abs_vec_A)
    print("|B| =", abs_vec_B)

main()