#Assignment 6.2
#Michael Gant
#20/04/2014
 
#Vector calculator
import math
vectorSum = []
vectorProd = 0
vectorNormA = 0
vectorNormB = 0

vectorA = input("Enter vector A:\n").split(" ") #recieves vectors as string
vectorB = input("Enter vector B:\n").split(" ")


for k in range(3):
    vectorSum.append(int(vectorA[k])+int(vectorB[k]))  #adds vectors
    vectorProd = vectorProd + int(vectorA[k])*int(vectorB[k]) #multiplies elements of vectors and then keeps a running total
    vectorNormA = vectorNormA + int(vectorA[k])*int(vectorA[k]) #square elements of vectors and then keeps a running total
    vectorNormB = vectorNormB + int(vectorB[k])*int(vectorB[k])
    
print("A+B = " + str(vectorSum))
print("A.B = " + str(vectorProd))
print("|A| = %.2f" % round(math.sqrt(vectorNormA),2)) #prints the root of the sum of the squares
print("|B| = %.2f" % round(math.sqrt(vectorNormB),2))
