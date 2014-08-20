"""a program to do basic vector calculations in 3 dimensions: 
addition, dot product and normalization
author: Barnett Msiska
date: 23/04/2014"""

import math

def main():
    A = collectVector('A')
    B = collectVector('B')
    addition = vectorAddition(A, B)
    print("A+B =", addition)
    dot = dotProduct(A,B)
    print("A.B =", dot)
    normA = norm(A)
    print("|A| =", "{0:.2f}".format(normA))
    normB = norm(B)
    print("|B| =", "{0:.2f}".format(normB))    
    
def collectVector(vectorName):
    """collects vector from usser as a string"""
    vectorString = input("Enter vector " + vectorName + ":\n")
    vector = vectorString.split(" ")
    intVector = []
    for n in vector:
        intVector.append(int(n))
    return(intVector)

def vectorAddition(vector1, vector2):
    """returns the sum of 2 vectors"""
    vectorSum = []
    for n in range(len(vector1)):
        for m in range(len(vector2)):
            if n == m:
                vectorSum.append(vector1[n] + vector2[m])
    return vectorSum

def dotProduct(vector1, vector2):
    """Returns the dot product of 2 vectors"""
    result = 0
    for n in range(len(vector1)):
        for m in range(len(vector2)):
            if n == m:
                result += vector1[n] * vector2[m]
    return result   

def norm(vector):
    """returns the norm of a vector"""
    result = 0
    for n in vector:
        result += n**2
    result = math.sqrt(result)
    return (round(result, 2))
main()