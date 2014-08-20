#Assignment 6
#Question 2
#Barry Su
#24 April 2014
#program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.

import math

#get vectors for A and B
a = input("Enter vector A:\n")
b = input("Enter vector B:\n")

#get the individual values in the vectors
lista = a.split(" ")
listb = b.split(" ")

#create list for the addition of each value in the two vectors
addition = []
for i in range(3):
    add = eval(lista[i]) + eval(listb[i])
    addition.append(add)
print("A+B =", addition)

#create list for the dot product of each value in the two vectors
product = []
for i in range(3):
    multiply = eval(lista[i])*eval(listb[i])
    product.append(multiply)
productSum = product[0] + product[1] + product[2]
print("A.B =", productSum)

#create list for normalization of each value in lista
normA = []
for i in range(3):
    sumOfSq = eval(lista[i])**2
    normA.append(sumOfSq)
answerA = math.sqrt(normA[0] + normA[1] + normA[2])
print("|A| = {0:0.2f}".format(answerA))

#create list for normalization of each value in listb
normB = []
for i in range(3):
    sumOfSq = eval(listb[i])**2
    normB.append(sumOfSq)
answerB = math.sqrt(normB[0] + normB[1] + normB[2])
print("|B| = {0:0.2f}".format(answerB))