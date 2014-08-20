# Assignment 6
# Program to calculate the sum, dot-product and normalized forms of two entered vectors
# Frans van Hoek   
# 22 April 2014

import math

def get_vector(a):
    ans = input("Enter vector "+a.upper()+":\n")
    vector = ans.split(" ")
    return vector

    
def add_vectors(a, b):
    vsum = []
    for i in range (3):
        isum = eval(a[i]) + eval(b[i])
        vsum.append(isum)
    return (vsum)


def dot_product(a, b):
    vpro = []
    dot_product = 0
    
    for i in range (3):
        ipro = eval(a[i])*eval(b[i])
        vpro.append(ipro)
        
    for item in vpro:
        dot_product += item
        
    return dot_product


def normalize(a):
    squares = []
    square_sum = 0
    vnormalized = 0
    
    for i in a:
        isq = eval(i)**2
        squares.append(isq)
        
    for i in squares:
        square_sum += i
        
    vnormalized = math.sqrt(square_sum)
    vnormalized = "{:.2f}".format(vnormalized)
    return vnormalized


def main():
    A = get_vector('A')
    B = get_vector('B')
    sumAB = add_vectors(A, B)
    proAB = dot_product(A,B)
    norA = normalize(A)
    norB = normalize(B)
    print("A+B =",sumAB)
    print("A.B =",proAB)
    print("|A| =", norA)
    print("|B| =", norB)
    
main()