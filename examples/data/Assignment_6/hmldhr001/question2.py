#Dhriven Hamlall

import math
def main():
    
    vectorA=input("Enter vector A:\n")
    vectorB=input("Enter vector B:\n")
    
    vectorA=vectorA.split(" ")
    vectorB=vectorB.split(" ") #split string into list ['4','7','3']
    
    vecDotProduct=0
    vectorSum=[] #list
    
    sumA=0
    sumB=0
    
    
    for i in range(len(vectorA)):
        
        vectorSum.append(int(vectorA[i])  +  int(vectorB[i]))
        vecDotProduct = vecDotProduct + (int(vectorA[i])  *  int(vectorB[i]))  
        
        sumA = sumA + (int(vectorA[i])**2)
        sumB = sumB + (int(vectorB[i])**2)
        
    print("A+B = ",end='')
    print(vectorSum)
    print("A.B = ",end='')
    print(vecDotProduct)
    
    print("|A| = {0:3.2f}".format(math.sqrt(sumA)))
    print("|B| = {0:3.2f}".format(math.sqrt(sumB)))
        
main()