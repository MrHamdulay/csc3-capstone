'''program to vector calculations on addition, dot product and normalization
question2, assignment6
Simangaliso mlangeni
MLNSIM014
24 April 2014'''

import math# imports math module
#create function to do vector addition
def vectorAdd(A,B):
#convert vectors from strings to lists 
    vectrA = A.split()
    vectrB = B.split()
#Add corresponding vector A & vector B components     
    xComp = eval(vectrA[0])+eval(vectrB[0])
    yComp = eval(vectrA[1])+eval(vectrB[1])
    zComp = eval(vectrA[2])+eval(vectrB[2])
    print("A+B = [",xComp,", ",yComp,", ",zComp,"]",sep="")#prints out the resulting vector from addition
    
#create function to calculate the dot product of two vectors    
def dotProduct(A,B):
    vectrA = A.split()
    vectrB = B.split()
#multiply corresponding components from vector A & vector B    
    xComp = eval(vectrA[0])*eval(vectrB[0])
    yComp = eval(vectrA[1])*eval(vectrB[1])
    zComp = eval(vectrA[2])*eval(vectrB[2])
    
    dotP = xComp+yComp+zComp#Adds components after vector multiplication to calculate dot product
    print("A.B =",dotP)#prints out the dot product of the two vectors                          

#create function to calculate
def normalization(A,B):
    vectrA = A.split()
    vectrB = B.split()    
#calculates the magnitude of each vector    
    magNA = math.sqrt((eval(vectrA[0])**2) + (eval(vectrA[1])**2) + (eval(vectrA[2])**2))
    magNB = math.sqrt((eval(vectrB[0])**2) + (eval(vectrB[1])**2) + (eval(vectrB[2])**2))
    
    if magNB == 0 and magNB == 0 :
        print("|A| = 0.00")
        print("|B| = 0.00")
    else:
        print("|A| =",round(magNA,2))
        print("|B| =",round(magNB,2))

#Request vectors from user    
A = input("Enter vector A:\n")
B = input("Enter vector B:\n")
vectorAdd(A,B)
dotProduct(A,B)
normalization(A,B)    