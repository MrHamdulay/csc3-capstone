"""question2.py
Author : Musa Xakaza
Date : 19/04/2014"""

import math

def get_Vector(l):
    """Gets a specified vector (l) from the user and returns it"""
    v = []
    stri = input("Enter vector "+l+":\n").split(' ')
    #Slice the string to get the elements/components of a vector
    for i in range(0,3):
        v.append(int(stri[i]))
    return v

def add(a,b):
    """Adds corresponding elements/components of 2 vectors """
    C = []
    for i in range(0,3):
        C.append(a[i]+b[i])
    return C

def dot(a,b):
    """Sums the products of corresponding elements/components vectors...
    ... & return a scalar quantity"""
    scalar = 0
    for i in range(0,3):
        scalar+= (a[i]*b[i])
    return scalar

def norm(v):
    """calculates the square root of the sum of the squares of the elements...
    ... rounded of to 2 decimal places"""
    sumOfSquares = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return '{0:0.2f}'.format(sumOfSquares)

def main():
    A = get_Vector("A")
    B = get_Vector("B")
    print("A+B = "+str(add(A,B)))
    print("A.B = "+str(dot(A,B)))
    print("|A| = "+str(norm(A)))
    print("|B| = "+str(norm(B)))
    
main()