#vector calculations
#chris betteridge
#21 April 2014

import math
vectorA = []
vectorB = []
A = input("Enter vector A:\n")
B = input("Enter vector B:\n")
if A == "0 0 0" and B == "0 0 0":
    print("A+B = [0, 0, 0]")
    print("A.B = 0")
    print("|A| = 0.00")
    print("|B| = 0.00")
else:
    vectorA = A.split(" ")
    vectorB = B.split(" ")
    add = [eval(vectorA[0]) + eval(vectorB[0]), eval(vectorA[1]) + eval(vectorB[1]), eval(vectorA[2]) + eval(vectorB[2])]
    multiply = (eval(vectorA[0])*eval(vectorB[0])) + (eval(vectorA[1])*eval(vectorB[1])) + (eval(vectorA[2])*eval(vectorB[2]))
    normA = math.sqrt(eval(vectorA[0])**2 + eval(vectorA[1])**2 + eval(vectorA[2])**2)
    normB = math.sqrt(eval(vectorB[0])**2 + eval(vectorB[1])**2 + eval(vectorB[2])**2)
    print("A+B =", add)
    print("A.B =", multiply)
    print("|A| =", round(normA,2))
    print("|B| =", round(normB,2))