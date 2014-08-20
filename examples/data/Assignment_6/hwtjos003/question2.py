import math
add = 0
dotProduct = 0
normA = 0
normB = 0

vectorA = []
vectorA = input("Enter vector A:\n").split(" ")
vectorB = []
vectorB = input("Enter vector B:\n").split(" ")

for i in range(3):
    vectorA[i] = eval(vectorA[i])
    vectorB[i] = eval(vectorB[i])
    dotProduct += vectorA[i] * vectorB[i]
    normA += vectorA[i] * vectorA[i]
    normB += vectorB[i] * vectorB[i]
    
add = "[" + str(vectorA[0] + vectorB[0]) + ", " + str(vectorA[1] + vectorB[1]) + ", " + str(vectorA[2] + vectorB[2]) + "]"
    
print("A+B = " + str(add), "A.B = " + str(dotProduct), "|A| = " + str('{0:.2f}'.format(math.sqrt(normA))), "|B| = " + str('{0:.2f}'.format(math.sqrt(normB))), sep = "\n")
    
    