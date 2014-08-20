#Question 2:Vector
#Galya Wolov
#23 April 2014

import math

#gets the vector A values and changes them into an array
stringA= input("Enter vector A:\n")
listA= stringA.split(" ")
evallistA= []
for item in listA:
    evallistA.append(eval(item))

#gets the vector B values and changes them into an array
stringB= input("Enter vector B:\n")
listB= stringB.split(" ")
evallistB= []
for item in listB:
    evallistB.append(eval(item))

#makes a new list: listAB which is listA + listB for each index of vector
listAB=[]
for i in range(0,3):
    listAB.append(evallistA[i] +evallistB[i])
print("A+B = ",(listAB),sep='')  

#adds the products of listA and ListB's same index
AB = (evallistA[0] *evallistB[0])+ (evallistA[1] *evallistB[1])+ (evallistA[2] *evallistB[2])
print("A.B = ",(AB),sep='') 

#provides the absolute value of A to 2 decimal points once it has put the index of a to the power of the same index of b and then square rooted the entire sum
absBofA = (evallistA[0]**2)+ (evallistA[1]**2)+ (evallistA[2]**2)
sqrt_ans1= math.sqrt(absBofA)
print("|A| = "+"{0:0.2f}".format(sqrt_ans1))

#provides the absolute value of B to 2 decimal points once it has put the index of b to the power of the same index of a and then square rooted the entire sum
absAofB = (evallistB[0] **2)+ (evallistB[1] **2)+ (evallistB[2] **2)
sqrt_ans2= math.sqrt(absAofB)
print("|B| = "+"{0:0.2f}".format(sqrt_ans2))