#Program to do basic vector calculations
#Kayla Hendricks
#23 April 2014

import math

def vectors():
    #starting with 3 items in list
    vA=[0,0,0]
    vB=[0,0,0]
    A=input("Enter vector A:\n")
    B=input("Enter vector B:\n")

    numA=0
    #splitting vectors up and evaluating them
    for i in A.split(" "):
        vA[numA]=eval(i)
        numA+=1
    
    numB=0
    #splitting vectors up and evaluating them
    for i in B.split(" "):
        vB[numB]=eval(i)
        numB+=1
    
    x = vA[0]**2+vA[1]**2+vA[2]**2
    y = vB[0]**2+vB[1]**2+vB[2]**2
    
    print("A+B = [",vA[0]+vB[0],", ",vA[1]+vB[1],", ",vA[2]+vB[2],"]",sep="")
    print("A.B =",vA[0]*vB[0]+vA[1]*vB[1]+vA[2]*vB[2])
    
    if vA[0] == 0 and vA[1] == 0 and vA[2] == 0:
        print("|A| = 0.00")
    else:
        print("|A| =",round(math.sqrt(x),2))
        
    if vB[0] == 0 and vB[1] == 0 and vB[2] == 0:
        print("|B| = 0.00")
    else:
        print("|B| =",round(math.sqrt(y),2))

vectors()
        
    