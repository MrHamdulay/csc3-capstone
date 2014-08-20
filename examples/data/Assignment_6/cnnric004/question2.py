import math

vectorStrA = input("Enter vector A:\n")
vectorA = vectorStrA.split(" ")
vectorStrB = input("Enter vector B:\n")
vectorB = vectorStrB.split(" ")

for k in range(len(vectorA)):
    vectorA[k] = eval(vectorA[k])
    vectorB[k] = eval(vectorB[k])

vectorAdd = [(vectorA[0]+vectorB[0]),(vectorA[1]+vectorB[1]),(vectorA[2]+vectorB[2])]
print("A+B =",vectorAdd)
vectorMultiply = ((vectorA[0]*vectorB[0]) +(vectorA[1]*vectorB[1])+(vectorA[2]*vectorB[2]))
print("A.B =", vectorMultiply)
vectorNormA = math.sqrt((vectorA[0])*(vectorA[0]) +(vectorA[1])*(vectorA[1]) +(vectorA[2])*(vectorA[2]))
print("|A| = ",end="")
print('{0000:.2f}'.format(vectorNormA))
vectorNormB = math.sqrt((vectorB[0])*(vectorB[0]) + (vectorB[1])*(vectorB[1]) + (vectorB[2])*(vectorB[2]))
print("|B| = ",end="")
print('{0000:.2f}'.format(vectorNormB))