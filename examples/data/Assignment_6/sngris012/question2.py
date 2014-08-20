#Rishen Singh SNGRIS012
#Question Two Assignment 6
import math #import math class
vectorA= input("Enter vector A:\n") #input first set of vectors
vectorB= input("Enter vector B:\n") #input second set of vectors

vecA= vectorA.split()#splits string at " "
vecB= vectorB.split()

vectorSum=[]
product=0
absA=0
absB=0
for i in range (3):
    vecA[i]=eval(vecA[i]) #converts value into integer
    vecB[i]=eval(vecB[i])
    vectorSum.append(vecA[i]+vecB[i])#adds sum of numbers into list
    product+=vecA[i]*vecB[i]#calculates product of each number in vector
    absA+=vecA[i]**2 #calculates sum of square of each number in vector
    absB+=vecB[i]**2

print("A+B =",vectorSum) #prints vectorSum
print("A.B =",product) #prints product of A and B
if (round(math.sqrt(absA),2))>0:
    print("|A| =",round(math.sqrt(absA),2))#prints the squareroot of all squares of vector
else:
    print("|A| = 0.00")

if (round(math.sqrt(absB),2))>0:
    print("|B| =",round(math.sqrt(absB),2))#prints the squareroot of all squares of vector
else:
    print("|B| = 0.00")

    