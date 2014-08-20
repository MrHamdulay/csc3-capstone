"""doing basic vector calculations in 3 dimensions
Lauren Denny
22 April 2014"""

import math

def addition(A,B):
    """return sum of 2 vectors A and B"""
    sum=[]
    for i in range(3):
        sum.append( eval(A[i])+eval(B[i]) ) # add corresponding elements and add to "sum" list
    return sum

def dot(A,B):
    """return dot product of two vectors A and B"""
    dot=0
    for i in range (3):
        dot+= eval(A[i])*eval(B[i]) #multiply corresponding elements and sum products
    return dot

def norm(A):
    """return norm of a vector A to 2 decimal places"""
    normtot=0
    for i in range(3):
        normtot+=eval(A[i])**2     #sum the squares of the elements 
    norm=math.sqrt(normtot)        #square root the sum
    return "{0:.2f}".format(norm)  #round to 2 decimals
    
def main():
    """get vectors A and B then print sum, dot product and two norms"""
    #get A and B and convert to lists
    A=input("Enter vector A:\n")
    A=A.split()
    B=input("Enter vector B:\n")
    B=B.split()    
    
    print("A+B =",addition(A,B))   #sum
    print("A.B =",dot(A,B))        #dot product
    print("|A| =",norm(A))         #norm of A
    print("|B| =",norm(B))         #norm of B

#run main function
main()