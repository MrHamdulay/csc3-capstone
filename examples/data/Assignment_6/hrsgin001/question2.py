#Gina Horscroft
#Assignment6
import math

a = input("Enter vector A:\n")
b = input("Enter vector B:\n")
#splits string into array
vectorA = a.split(" ")
vectorB =b.split(" ")

sumN = []
prodN = []
prodF = 0
newA = []
newB = []
sqrtA = 0
sqrtB = 0
for i in range (len(vectorA)):
    #converts strings in array to integers in new arrays
    newA.append(int(vectorA[i]))
    newB.append(int(vectorB[i]))

    sumN.append(newA[i] + newB[i])
    prodN.append(newA[i] * newB[i])
    prodF += prodN[i]
    sqrtA+= newA[i]**2
    sqrtB+= newB[i]**2    
sqrtA = round(math.sqrt(sqrtA), 2)
sqrtB = round(math.sqrt(sqrtB), 2)

print("A+B =", sumN)
print("A.B =", prodF)

#different formatting because when given 0, round displays 0.0 instead of 0.00
formA = '{:.2f}'.format(sqrtA)
formB = '{:.2f}'.format(sqrtB)
print("|A| =", formA)
print("|B| =", formB)

