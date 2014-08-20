inputA = input("Enter vector A:\n")
vectorA = inputA.split()
vectorA[0] = eval(vectorA[0])
vectorA[1] = eval(vectorA[1])
vectorA[2] = eval(vectorA[2])

inputB = input("Enter vector B:\n")
vectorB = inputB.split()
vectorB[0] = eval(vectorB[0])
vectorB[1] = eval(vectorB[1])
vectorB[2] = eval(vectorB[2])


Sum = []
for i in range(3):
    Sum.append(vectorA[i]+vectorB[i])
print("A+B =",Sum)

multi = 0
for i in range(3):
    multi = multi + (vectorA[i]*vectorB[i])
print("A.B =",multi)


import math
normalA = math.sqrt((vectorA[0]*vectorA[0]+vectorA[1]*vectorA[1]+vectorA[2]*vectorA[2]))
normalB = math.sqrt((vectorB[0]*vectorB[0]+vectorB[1]*vectorB[1]+vectorB[2]*vectorB[2]))
print("|A| =","{0:0.2f}".format(normalA))
print("|B| =","{0:0.2f}".format(normalB))
    
