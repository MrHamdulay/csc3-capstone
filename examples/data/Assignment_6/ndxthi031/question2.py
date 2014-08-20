"""voting program
Thiolan Prevan Naidoo
NDXTHI031
25 april 2014"""

import math 
vA= input("Enter vector A:\n") 
vB= input("Enter vector B:\n") 

vecA= vA.split()#splits string to list VecA at occurence of a space
vecB= vB.split()
#initialise variables
vSum=[]
product=0
absA=0
absB=0

for i in range (3):
    vecA[i]=eval(vecA[i]) #converts string value in list into integer
    vecB[i]=eval(vecB[i])
    
    vSum.append(vecA[i]+vecB[i])#adds sum of numbers into list
    
    product+=vecA[i]*vecB[i]#calculates product of each number in vector
    
    absA+=vecA[i]**2 #calculates sum of square of each number in vector
    absB+=vecB[i]**2

print("A+B =",vSum) 
print("A.B =",product) 

if (round(math.sqrt(absA),2))>0:
    print("|A| =",round(math.sqrt(absA),2))#prints the squareroot of all squares of vector A
else:
    print("|A| = 0.00")

if (round(math.sqrt(absB),2))>0:
    print("|B| =",round(math.sqrt(absB),2))#prints the squareroot of all squares of vector B
else:
    print("|B| = 0.00")

    