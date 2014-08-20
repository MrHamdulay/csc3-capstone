# Luke Henkeman
# HNKLUK001
# 25 April 2014
# question2.py
# basic vector calcs in 3-d
# addition, dot product, normalisation

import math

def vectors():
    vctrA = input("Enter vector A:\n")
    vctrB = input("Enter vector B:\n")
    vctrA = vctrA.split(" ")
    vctrB = vctrB.split(" ")
    iA0 = int(vctrA[0])
    iA1 = int(vctrA[1])
    iA2 = int(vctrA[2])
    iB0 = int(vctrB[0])
    iB1 = int(vctrB[1])
    iB2 = int(vctrB[2])
    add = [iA0+iB0, iA1+iB1, iA2+iB2]
    print("A+B =",add)
    dot = int(iA0*iB0 + iA1*iB1 + iA2*iB2)
    print("A.B =",dot)
    normA = round(math.sqrt(iA0**2 + iA1**2 + iA2**2),2)
    normB = round(math.sqrt(iB0**2 + iB1**2 + iB2**2),2)
    print("|A| =",normA)
    print("|B| =",normB)
    
vectors()