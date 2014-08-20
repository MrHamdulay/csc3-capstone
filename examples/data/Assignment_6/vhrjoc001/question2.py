#Iassignment 6 question 2
#vhrjoc001
#doing vector addition,dot and cross product

from math import sqrt

a1, a2, a3 = input("Enter vector A:\n").split()  #getting input and assigning variableds for input
vector_a = [int(a1), int(a2), int(a3)]
b1, b2, b3 = input("Enter vector B:\n").split()
vector_b = [int(b1), int(b2), int(b3)]

def vectorAdd(a, b):       #vector addition
    resultVector = []
    for i in range(len(a)):
        result = a[i] + b[i]
        resultVector.append(result)
    return resultVector

def vectorDot(a, b):    #vector dot product
    resultAlpha = 0
    for i in range(len(a)):
        result = a[i] * b[i]
        resultAlpha += result
    return resultAlpha

def vectorNorm(a):      #magnitude of vector
    finalResult = 0
    for i in range(len(a)):
        result = a[i]**2
        finalResult += result
    finalResult = sqrt(finalResult)
    return finalResult

print("A+B =",vectorAdd(vector_a, vector_b))
print("A.B =",vectorDot(vector_a, vector_b))
if vectorNorm(vector_a)==0:     #needed due to round off function error when magnitude is 0
    print("|A| = 0.00")
else:
    print("|A| =",round(vectorNorm(vector_a),2))
if vectorNorm(vector_b)==0:
    print("|B| = 0.00")
else:
    print("|B| =",round(vectorNorm(vector_b),2)) 