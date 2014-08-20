#Assignment 6
#question 2

import math 

#Get values for vector from user
vectorA= input("Enter vector A:\n")
vectorB= input("Enter vector B:\n")

#Create a list using given inputs
vectorA= vectorA.split(" ")
vectorB= vectorB.split(" ")
#print(vectorA)
#print(vectorB)

#Addition of vectors
add0= eval(vectorA[0])+eval(vectorB[0])
add0= round(add0,2)
add1= eval(vectorA[1])+eval(vectorB[1])
add1=round(add1,2)
add2= eval(vectorA[2])+eval(vectorB[2])
add2= round(add2,2)
print("A+B = [", end="")
print(add0, add1, add2, sep=", ",end="]\n")

#Dot product
product0= eval(vectorA[0])*eval(vectorB[0])
product1= eval(vectorA[1])*eval(vectorB[1])
product2= eval(vectorA[2])*eval(vectorB[2])
add_product= round(product0+product1+product2, 2)
print("A.B =",add_product, end="\n")

#Normalization
normA= math.sqrt((eval(vectorA[0])**2+eval(vectorA[1])**2+eval(vectorA[2])**2))
normB= math.sqrt((eval(vectorB[0])**2+eval(vectorB[1])**2+eval(vectorB[2])**2))
if normA==0 and normB!=0:
    print("|A| = 0.00")
    print("|B| =", round(normB,2))
elif normA==0 and normB==0:
    print("|A| = 0.00")
    print("|B| = 0.00")
elif normB==0 and normA!=0:
    print("|A| =", round(normA,2))
    print("|B| = 0.00")
else: 
    print("|A| =", round(normA,2))
    print("|B| =", round(normB,2))








              
