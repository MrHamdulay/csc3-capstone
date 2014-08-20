"""Program to do basic vector calculations in 3 dimensions
Tamsin Kantor
20 April 2014"""

import math

# creating vector A
A = input("Enter vector A:\n")
A = A.split(" ") # making a list
A = [eval(i) for i in A] # converting all list items from strings to ints

# creating vector B
B = input("Enter vector B:\n")
B = B.split(" ") # making a list
B = [eval(i) for i in B] # converting all list items from strings to ints

def addition(A,B):
    C = [0,0,0]
    C[0] = A[0]+B[0]
    C[1] = A[1]+B[1]
    C[2] = A[2]+B[2]
    print ("A+B =",C)

def dotproduct(A,B):
    C = A[0]*B[0] + A[1]*B[1] + A[2]*B[2]
    print ("A.B =",C)    

def normalizationA(A,B):
    C = math.sqrt( A[0]*A[0] + A[1]*A[1] + A[2]*A[2] )
    print ("|A| =", "{0:.2f}".format(C) )

def normalizationB(A,B):
    C = math.sqrt( B[0]*B[0] + B[1]*B[1] + B[2]*B[2] )
    print ("|B| =", "{0:.2f}".format(C) )

# calling all the functions
addition(A,B)
dotproduct(A,B)
normalizationA(A,B)
normalizationB(A,B)