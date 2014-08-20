#Vector calculations in 3 dimensions
#Question 2
#Annie Ho
#24/04/2014

import math


A= input ("Enter vector A: \n")
B= input ("Enter vector B: \n")

listx = A.split(" ")
listy = B.split(" ")

addition = []
for i in range(3):
    add = eval(listx[i]) + eval(listy[i])
    addition.append(add)
print("A+B =", addition)

prct = []
for i in range(3):
    multi = eval(listx[i])*eval(listy[i])
    prct.append(multi)
answer= prct[0] + prct[1] + prct[2]
print("A.B =", answer)

normal = []
for i in range(3):
    sumofSq = eval(listx[i])**2
    normal.append(sumofSq)
answerA = math.sqrt(normal[0] + normal[1] + normal[2])
print("|A| = {0:0.2f}".format(answerA))

normB = []
for i in range(3):
    sumofSq = eval(listy[i])**2
    normB.append(sumofSq)
answerB = math.sqrt(normB[0] + normB[1] + normB[2])
print("|B| = {0:0.2f}".format(answerB))