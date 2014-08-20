"""program to do basic vector calculations in 3 dimensions: addition, dot product and normalisation"""
#Bandon Pickup (PCKBRA002)
#2014/04/21
#Assignment 6 Question 2
import math
vectorA = input("Enter vector A:\n").split(" ")#splits the inpout into a list of 3 seperate numbers
vectorB = input("Enter vector B:\n").split(" ")
additionList=[]
product=0
aNorm=0
bNorm=0
for i in range(3):#for loop that only runs three times because the vectors are only 3 dimensional
    additionList.append(int(vectorA[i])+int(vectorB[i]))#list of addition vectors is appended by adding the vector A and vector B of identical positions
    product+=int(vectorA[i])*int(vectorB[i])#adds the product of the vectors in the same position to the total product variable
    aNorm += int(vectorA[i])**2#adds the square of the current vector
    bNorm += int(vectorB[i])**2
print ("A+B =",additionList)
print ("A.B =",product)
if aNorm == 0 or bNorm == 0:
    print("|A| = 0.00")
    print("|B| = 0.00")
else:
    print("|A| =",round(math.sqrt(aNorm),2))#prints normalised A - squareroot of aNorm rounded to 2 decimal places
    print("|B| =",round(math.sqrt(bNorm),2))
