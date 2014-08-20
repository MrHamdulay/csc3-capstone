"""Question 2, Assignment 6
Tejasvin Bagirathi BGRTEJ001"""

import math

inputA = input('Enter vector A:\n')
inputB = input('Enter vector B:\n')

#Split up input list
inputA = inputA.split(' ')
inputB = inputB.split(' ')

#Declare lists
vecA = []
vecB = []

#Convert inputB to integers and append to list
for i in range(len(inputA)):
    x = inputA[i]
    x = int(x)
    vecA.append(x)

#Convert inputB to integers and append to list
for j in range(len(inputB)):
    y = inputB[j]
    y = int(y)
    vecB.append(y)
    
sumab = []
product = 0
normA = float(0)
normB = float(0)

for a in range(3):
    #Add vector A and B
    aplusb = vecA[a] + vecB[a]
    sumab.append(aplusb)
    #Calculate product of A.B
    ab = vecA[a]*vecB[a]
    product+=ab
    #Calculate norm of A and convert list item to float
    rootA = float(vecA[a]**2)
    normA += rootA
    #Calculate norm of B and convert list item to float
    rootB = float(vecB[a]**2)
    normB += rootB    

#Print out vector calculations
print('A+B =', sumab)
print('A.B =', product)
print('|A| =', '{0:0.2f}'.format(math.sqrt(normA)))
print('|B| =','{0:0.2f}'.format(math.sqrt(normB)))