#Program to do basic vector calculations
#Annika Brundyn
#24/04/2014 

import math

#Get the inputs from user and convert to a list
vectorA = input("Enter vector A:\n")
vectorB = input("Enter vector B:\n")

A = vectorA.split(" ")
B = vectorB.split(" ")


#Convert strings to integers
A = [int(i) for i in A]
B = [int(i) for i in B]


#addition
print("A+B = [",(A[0]+B[0]),", ",(A[1]+B[1]),", ",(A[2]+B[2]),"]",sep="")

#dot product
print("A.B =",((A[0]*B[0])+(A[1]*B[1])+(A[2]*B[2])))

#normalizationA
normA = math.sqrt((A[0]**2)+(A[1]**2)+(A[2]**2))
if A[0]==0 and A[1]==0 and A[2]==0: 
    print("|A| = 0.00")
else:
    print("|A| =",round(normA,2))

#normalizationB
normB = math.sqrt((B[0]**2)+(B[1]**2)+(B[2]**2))
if B[0]==0 and B[1]==0 and B[2]==0:
    print("|B| = 0.00")
else:    
    print("|B| =",round(normB,2))
