#Question 2
#Vector calculations
#By: Dean de Haast
import math

def main():
    vecA=[]
    vecB=[]
    addition=[0,0,0]
    dotproduct=0
    modA = 0
    modB = 0
    
    #assigning vectors to lists
    vectorA=input("Enter vector A:\n")
    vecA=vectorA.split()
    vectorB=input("Enter vector B:\n")
    vecB=vectorB.split()   
    # Doing the calculations 
    for i in range (3):
        addition[i]= eval(vecA[i]) +eval(vecB[i])
        dotproduct += eval(vecA[i]) *eval(vecB[i])
        modA+=((eval(vecA[i]))**2)
        modB+=((eval(vecB[i]))**2)
    #Completing the square root part of the ABS   
    modA=(math.sqrt(modA))
    modB=(math.sqrt(modB))
    
    print ("A+B =",addition)
    print("A.B =",dotproduct)
    print("|A| =","{0:.2f}".format(modA))
    print("|B| =","{0:.2f}".format(modB))
        
main()
    
