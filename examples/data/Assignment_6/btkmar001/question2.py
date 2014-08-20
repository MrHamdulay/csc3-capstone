# question2.py
# a programm for adding, dotmultipying and norm operations with vectors
# Martin Batek
# BTKMAR001
# 22 April 2014

import math

def addvector(vector1,vector2): # returns vector addition
    answer = []
    for i in range(3):
        answer.append(vector1[i] + vector2[i])
    return answer

def dotproduct(vector1,vector2): #returns vector dotproducts
    answer = 0
    for i in range(3):
        answer += vector1[i]*vector2[i]
    return answer

def norm(vector): # returns norm operations
    import math
    add = 0
    for i in range(3):
        add += (vector[i])**2
    answer = math.sqrt(add)
    return answer

def convert(strvector): # Converts a list of numeric strings to a list of numbers
    lofstr = strvector.split(" ")
    numvector = []
    for i in range(len(lofstr)):
        numvector.append(eval(lofstr[i]))
    return numvector

vectorA = input("Enter vector A:\n")
vectorA = convert(vectorA)
vectorB = input("Enter vector B:\n")
vectorB = convert(vectorB)

print("A+B =", addvector(vectorA,vectorB))
print("A.B =", dotproduct(vectorA,vectorB))
print("|A| =", "{:.2f}".format(norm(vectorA)))
print("|B| =", "{:.2f}".format(norm(vectorB)))