#Calculations with vectors
#Keanon Fell
#24 April 2014

import math

print("Enter vector A:")
vectorA = input()
print("Enter vector B:")
vectorB = input()

listA = vectorA.split(" ")
listB = vectorB.split(" ")

sumList = []
if len(listA) == len(listB):
    for i in range(len(listA)):
        sum = eval(listA[i]) + eval(listB[i])
        sumList.append(sum)
print("A+B = ",sumList,sep="")

sum=0
if len(listA) == len(listB):
    for k in range(len(listA)):
        product = eval(listA[k])* eval(listB[k])
        sum+=product
print("A.B =", sum)


squareA = 0
for a in range(len(listA)):
    square = eval(listA[a])**2
    squareA += square
x = math.sqrt(squareA)
if not listA == ["0","0","0"]:
    print("|A| =",round(x,2))
else:
    print("|A| = 0.00")

squareB = 0
for b in range(len(listB)):
    square = eval(listB[b])**2
    squareB += square
x = math.sqrt(squareB)
if not listB == ["0","0","0"]:
    print("|B| =",round(x,2))
else:
    print("|B| = 0.00")