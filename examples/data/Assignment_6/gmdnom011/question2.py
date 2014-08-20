# Program to do basic vector calculations
# Nomsa Gamedze
# 21 April 2014

import math

def get_vector(n):
    prompt = "Enter vector " + n + ":" + '\n'
    s_vector = input(prompt)
    s_list_vector = s_vector.split()
    vector = []
    for i in s_list_vector:
        value = eval(i)
        vector.append(value)
    return vector

def add_vectors(A, B):
    added = []
    for i in range(3):
        value = A[i]+B[i]
        added.append(value)
    return added

def multiply_vectors(A, B):
    product = 0
    for i in range(3):
        value = A[i]*B[i]
        product += value
    return product

def abs_vector(A):
    squares = 0
    for i in range(3):
        value = A[i]**2
        squares += value
    mod = math.sqrt(squares)
    mod = round(mod, 2)
    s_mod = str(mod)
    l = len(s_mod)
    point = s_mod.index(".")
    diff = l - point
    if diff == 2:
        s_mod += "0"
        mod = s_mod
    return mod

def main():
    A = get_vector("A")
    B = get_vector("B")
    print("A+B =", add_vectors(A, B))
    print("A.B =", multiply_vectors(A, B))
    print("|A| =", abs_vector(A))
    print("|B| =", abs_vector(B))
    
main()    