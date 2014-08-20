""" a program to do basic vector calculations in 3 dimensions: addition, 
dot product and normalization
Author: Dominic Manthoko
21 April 2014
"""

def v_add(A,B):
    """ function that adds two vectors together"""
    
    # sum the corresponding vector components together
    x_com = int(A[0]) + int(B[0])
    y_com = int(A[1]) + int(B[1])
    z_com = int(A[2]) + int(B[2])
    
    # add all the component additions
    add = [x_com, y_com, z_com]
    
    return add

def dot_product(A,B):
    """ function that calculates the dot product of two vectors """
    
    # multiply the corresponding vector components
    x_com = int(A[0]) * int(B[0])
    y_com = int(A[1]) * int(B[1])
    z_com = int(A[2]) * int(B[2])
    
    mul = x_com + y_com + z_com
    
    return mul

# need the math module in order to find the square root of something in the 
# v_norm function
import math

def v_norm(V):
    """ function to calculate the norm of a single vector """
    
    # raise each vector component to the power of 2
    x_com = int(V[0]) ** 2
    y_com = int(V[1]) ** 2
    z_com = int(V[2]) ** 2
    
    # find the root of the sum of the vector components squared
    norm = math.sqrt(x_com + y_com + z_com)
    
    return norm

def main():
    # prompt the user to enter two vectors
    A = input("Enter vector A: \n")
    A = A.split()
    
    B = input("Enter vector B: \n")
    B = B.split()
    
    print('A+B = {}'.format(v_add(A,B)))
    print('A.B = {}'.format(dot_product(A,B)))
    print('|A| = {0:0.2f}'.format(v_norm(A)))
    print('|B| = {0:0.2f}'.format(v_norm(B)))
    
if __name__ == '__main__' :
    main()