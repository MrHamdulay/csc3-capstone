#program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
import math
arrA = []
arrB = []

#Get first vector
stringA = input("Enter vector A:\n")
stringB = input('Enter vector B:\n')

#Enter values into array
for n in stringA.split():
    arrA.append(eval(n))
for v in stringB.split():
    arrB.append(eval(v))

#Add vectors
Sum = []
for i in range(3):
    addition =arrA[i]+arrB[i]
    Sum.append(addition)
print("A+B =",Sum)

#Mutliply Vectors
total=0
for j in range(3):
    multiplication = arrA[j]*arrB[j]
    total+=multiplication
print("A.B =",total)

#Get Norm of single vector
rootA=0
for k in range(3):
    rootA+= arrA[k]**2
    s= "{0:0.2f}"
    resultA = math.sqrt(rootA)
print("|A| =",s.format(resultA))

rootB=0
for l in range(3):
    rootB+= arrB[l]**2
    s= "{0:0.2f}"
    resultB = math.sqrt(rootB)    
print("|B| =",s.format(resultB))