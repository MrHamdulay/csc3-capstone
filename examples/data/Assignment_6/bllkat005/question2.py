# Kate Bell
# BLLKAT005
# 22 April 2014 

import math

def addVectors(vectorA, vectorB):
    """Add two vectors"""
    add = []
    for i in range(len(vectorA)):
        add.append(eval(vectorA[i])+eval(vectorB[i]))
    return add

def dotProduct(vectorA, vectorB):
    """Dot product of two vectors"""
    product =0
    for i in range(len(vectorA)):
            product += eval(vectorA[i])*eval(vectorB[i])
    return product   

def normalise(vectorA):
    """Normalization of a vector"""
    normal = 0
    for i in range(len(vectorA)):
        normal += eval(vectorA[i])*eval(vectorA[i])
    return round(math.sqrt(normal),2)

def main():
    vectorA = input("Enter vector A:\n").split(" ")
    vectorB = input("Enter vector B:\n").split(" ")
    
    add_vectors = addVectors(vectorA,vectorB)
    print("A+B =",add_vectors)
    
    print("A.B =",dotProduct(vectorA, vectorB))
    
    a = normalise(vectorA)
    if a == 0.0:
        print("|A| = 0.00")
    else: print("|A| =",a)
    
    b = normalise(vectorB)
    if b == 0.0:
        print("|B| = 0.00")
    else: print("|B| =",b)    
    
if __name__ == "__main__":
    main()
