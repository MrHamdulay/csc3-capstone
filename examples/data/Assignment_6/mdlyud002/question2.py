# Yudhi Moodley
# Assignment 6 - Vector Calculator
# 23/04/2014

import math

vectorA = []
vectorB = []
addition = []
dotProduct = []
normalization = []

def vector_calculator():
    vector1 = input("Enter vector A:\n")
    vectorA = vector1.split(' ') # splits the input
    
    vector2 = input("Enter vector B:\n")
    vectorB = vector2.split(' ') # splits the input

# addition funtion    
    for i in range (3):
        addNum = eval(vectorA[i]) + eval(vectorB[i])
        addition.append(addNum)
    print("A+B = [" + str(addition[0]) + ", " + str(addition[1]) + ", " + str(addition[2]) + "]") 
    
# calculates the funtion of the vector    
    for i in range (3):
        multNum = eval(vectorA[i]) * eval(vectorB[i])
        dotProduct.append(multNum)
    product = 0
    
    for i in range (3):
        product += dotProduct[i]
    print("A.B = " + str(product))
    
# normalizes the vector
    aSum = eval(vectorA[0])**2 + eval(vectorA[1])**2 + eval(vectorA[2])**2
    aRoot = ("{0:.2f}".format(math.sqrt(aSum)))
    print("|A| =",aRoot)
    
    bSum = eval(vectorB[0])**2 + eval(vectorB[1])**2 + eval(vectorB[2])**2
    bRoot = ("{0:.2f}".format(math.sqrt(bSum)))
    print("|B| =",bRoot)

vector_calculator()