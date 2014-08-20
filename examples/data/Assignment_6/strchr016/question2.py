"""Simple vector arithmatic
Christopher Sterley
20/04/2014"""

#Import math functions
import math

#Get vectors to work with
VecA=input("Enter vector A:\n")
VecA=VecA.split()

VecB=input("Enter vector B:\n")
VecB=VecB.split()

#Function for the sum of vectors
def sumvec(VecA,VecB):
    sum=[]
    for i in range(3):
        sum.append(int(VecA[i])+int(VecB[i]))
    return sum

#Function for the dot product of vectors
def dotvec(VecA,VecB):
    dotprod=0
    for i in range(3):
        dotprod+=(int(VecA[i])*int(VecB[i]))
    return dotprod

#Function for normalisation of vectors for the given inputs
def normvecA(VecA):
    normA=0
    
    for i in range(3):
        normA+=(int(VecA[i]))**2
        
    return "{:.2f}".format(math.sqrt(normA))


#Return relevant outputs
print("A+B =", sumvec(VecA,VecB))
print("A.B =", dotvec(VecA,VecB))
print("|A| =", normvecA(VecA))
print("|B| =", normvecA(VecB))