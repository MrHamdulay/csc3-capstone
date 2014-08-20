"""CSC1015F Assignment 6 Question 2
Xola Matlanyane MTLXOL002
25 April 2014"""

import math

#Enter the vectors
VA=input("Enter vector A:\n")
VB=input("Enter vector B:\n")

#Splitting the string
VA = VA.split(" ")
VB = VB.split(" ")

#Make variables to hold the results of functions
sumv=[]
dotv=0
norma=0
normb=0

#Run loop to access elements
for i in range(3):
    #Convert strings to integers
    VA[i] = int(VA[i])
    VB[i] = int(VB[i])
    
    #Sum
    sumv.append(VA[i]+ VB[i])
    #Product
    dotv+= VA[i]*VB[i]
    #|A|
    norma+= VA[i]**2
    #|B|
    normb+= VB[i]**2
    
#Squareroot the norms
norma=math.sqrt(norma)
normb=math.sqrt(normb)

print("A+B =",sumv)
print("A.B =", dotv)
print("|A| = {0:.2f}".format(round(norma, 2)))
print("|B| = {0:.2f}".format(round(normb, 2)))
