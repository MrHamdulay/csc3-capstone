#SNGSOH004
#Assignment 6
#Question 1
#23rd April 2014

import math
vectorA, vectorB = [], [] #creating the empty arrays

tempA = input("Enter vector A:\n").split(" ")
vectorA = [tempA[0], tempA[1], tempA[2]] #storing the vectors

tempB = input("Enter vector B:\n").split(" ")
vectorB = [tempB[0], tempB[1], tempB[2]] #storing the vectors

aplusb = [(eval(vectorA[0]))+(eval(vectorB[0])), (eval(vectorA[1]))+(eval(vectorB[1])), (eval(vectorA[2]))+(eval(vectorB[2]))] #storing the sum of the vectors in a new list
adotb = (eval(vectorA[0])*eval(vectorB[0])) + (eval(vectorA[1])*eval(vectorB[1])) + (eval(vectorA[2])*eval(vectorB[2])) #calculating the dot product and storing it in a list
normA = math.sqrt(eval(vectorA[0])**2 + eval(vectorA[1])**2 + eval(vectorA[2])**2) #calculating the norm
normB = math.sqrt(eval(vectorB[0])**2 + eval(vectorB[1])**2 + eval(vectorB[2])**2) #calculating the norm

print("A+B = "+str(aplusb))
print("A.B = "+str(adotb))
print("|A| = {:.2f}".format(normA))
print("|B| = {:.2f}".format(normB))