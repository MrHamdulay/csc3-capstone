#Charles Schleich SCHCHA027
#Question 2 Assignment 6

import math
# defining all the variables
vectorA=input("Enter vector A:\n")
vectorA= vectorA.split()
vectorB=input("Enter vector B:\n")
vectorB= vectorB.split()
newvector=[0,0,0]
# for loop that adds vectors
for i in range(3):
    vectaddA=eval(vectorA[i])
    vectaddB=eval(vectorB[i])
    addedvect= vectaddA+vectaddB
    newvector[i]=addedvect
print("A+B = ",newvector,sep="")

mult=0
# for loop multipllies vectors
for k in range(3):
    vectmultA=eval(vectorA[k])
    vectmultB=eval(vectorB[k])    
    mult= (vectmultA*vectmultB)
   # print(mult,"=", (vectmultA),(vectmultB))
    newvector[k]=mult
total=newvector[0]+newvector[1]+newvector[2]

print("A.B = ",total,sep="")

totalA,totalB=0,0
# for loop that adds square vectors
for p in range(3):
    vecttotA=eval(vectorA[p])
    vecttotB=eval(vectorB[p])    
    totalA=totalA+(vecttotA**2) 
    totalB=totalB+(vecttotB**2)
# final output for A and B 
print("|A| = ","%0.2f" %  (math.sqrt(totalA)),sep="")
    
print("|B| = ","%0.2f" % (math.sqrt(totalB)),sep="")
