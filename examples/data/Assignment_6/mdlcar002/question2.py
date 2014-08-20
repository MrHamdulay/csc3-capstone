#assignment6 Question2
#Carissa Moodley
#basic vector calculations in three dimensions

import math
def main():
    vectorA=input("Enter vector A:\n")
    vectorB=input("Enter vector B:\n")
    
    #converting string to list
    vectorA=vectorA.split(" ")
    vectorB=vectorB.split(" ")
    
    
    vectorsum=[]
    vectorproduct=0
    sumA=0
    sumB=0
    
    for i in range(3):
        vectorsum.append(int(vectorA[i])+int(vectorB[i]))
        vectorproduct+=(int(vectorA[i])*int(vectorB[i]))
        sumA+=(int(vectorA[i])**2)
        sumB+=(int(vectorB[i])**2)
   
    print("A+B =",vectorsum) 
    print("A.B =",vectorproduct)
    print("|A| = {0:3.2f}".format(math.sqrt(sumA)))
    print("|B| = {0:3.2f}".format(math.sqrt(sumB)))
    
    NormA=0
    NormB=0
    for i in range(3):
            sum    
    
main()