"""Assignment 6 Question 2
Johan Jansen van Vuuren (JNSJOH014)
21 April 2014"""
import math

def main():
    vectorA = []
    vectorB = []

    #get and process input
    tempA = (input("Enter vector A:\n")).split(" ")
    tempB = (input("Enter vector B:\n")).split(" ")
    for i in tempA:
        vectorA.append(eval(i))
    for i in tempB:
        vectorB.append(eval(i))

    print("A+B =",getSum(vectorA,vectorB))
    print("A.B =",getDotProduct(vectorA,vectorB))
    print("|A| = %.2f"%float(norm(vectorA)))
    print("|B| = %.2f"%float(norm(vectorB)))

def getSum(vectorA,vectorB):
    result = []
    for i in range(3):
        result.append(vectorA[i]+vectorB[i])
    return result

def getDotProduct(vectorA,vectorB):
    result = []
    for i in range(3):
        result.append(vectorA[i]*vectorB[i])
    return result[0]+result[1]+result[2]

def norm(vector):
    result = round(((vector[0]**2+vector[1]**2+vector[2]**2)**0.5),2)
    return result

if __name__=="__main__":
    main()