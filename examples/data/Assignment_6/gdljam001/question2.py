"""Vector Calculations
James Godlonton
23 April 2014"""
import math
def addition(vecA,vecB):#Uses vector addition to add 2 given vectors and returns answer
    retVector=[]
    for i in range(3):#Adds each sum to dimension in new vector
        retVector.append(int(vecA[i])+int(vecB[i]))
    return retVector

def dotProduct(vecA,vecB):#Takes the dot product of 2 given vectors and returns wanted value
    retVal=0
    for i in range(3):#Goes through adding the product of the respectable dimensions
        retVal=retVal+(int(vecA[i])*int(vecB[i]))
    return retVal

def norm(vecA):#return the normalization (as a string) of a given vector
    total=0;
    for i in range(3):#Goes through vector squaring each element and adding it to total
        total=total+(int(vecA[i]))**2
    
        
    number= math.sqrt(total)
    number=round(number,2)
    if len(str(number).split(".")[1])==1:#Checking to see that there are 2 numbers after the decimal, if not then adding "0"
        number=str(number)+"0"
    return str(number)#returns the rounded off string
    
    
        
        

    
def main():#Input and output is handled
    vecA=input("Enter vector A:\n")
    vecA=vecA.split(" ")
    vecB=input("Enter vector B:\n")
    vecB=vecB.split(" ")
    print("A+B = "+str(addition(vecA,vecB)))
    print("A.B = "+str(dotProduct(vecA,vecB)))
    print("|A| = "+norm(vecA))
    print("|B| = "+norm(vecB))
    
    
if __name__=="__main__":
    main()
    
    