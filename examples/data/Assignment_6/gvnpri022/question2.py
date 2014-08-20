"""question 2-assignment 6- vector calculations
GVNPRI022
23 April 2014"""
import math
#splitting input into arrays
aList = input("Enter vector A:\n").split(" ") 
bList = input("Enter vector B:\n").split(" ")
for j in range (len(aList)): #evaluating arrays
    
    aList[j]= eval(aList[j])
    bList[j]= eval(bList[j])
sumVector=[]
prodSum=0
aNormalise=0
bNormalise=0
for i in range(len(aList)): 
    sumVector.append(aList[i]+bList[i]) #finding sum of vectors
    prodSum= prodSum + (aList[i]*bList[i]) #finding product of vectors
    aNormalise= aNormalise+ aList[i]**2 #norm of A
    bNormalise= bNormalise + bList[i]**2 #norm of B
#Output Statements    
print("A+B =",sumVector)
print("A.B =",prodSum)
aNorm= "{0:0.2f}".format(math.sqrt(aNormalise))
bNorm= "{0:0.2f}".format(math.sqrt(bNormalise))

print("|A| =",aNorm)
print("|B| =",bNorm)

