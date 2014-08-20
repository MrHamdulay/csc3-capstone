#Assignment 6
#Question 2
#Helin Kim

#basic vector calculations in 3 dimensions: addition, dot product and normalization

import math


vectora = input("Enter vector A:\n")
vectorb = input("Enter vector B:\n")


lista = vectora.split(" ")
listb = vectorb.split(" ")


addition = []


for i in range(3):
    
    add = eval(lista[i]) + eval(listb[i])
    addition.append(add)
    
print("A+B =", addition)


product = []
for i in range(3):
    multiply = eval(lista[i])*eval(listb[i])
    product.append(multiply)
productSum = product[0] + product[1] + product[2]
print("A.B =", productSum)


normalA = []
for i in range(3):
    sumOfSquare = eval(lista[i])**2
    normalA.append(sumOfSquare)
ansA = math.sqrt(normalA[0] + normalA[1] + normalA[2])
print("|A| = {0:0.2f}".format(ansA))


normalB = []
for i in range(3):
    sumOfSquare = eval(listb[i])**2
    normalB.append(sumOfSquare)
ansB = math.sqrt(normalB[0] + normalB[1] + normalB[2])
print("|B| = {0:0.2f}".format(ansB))