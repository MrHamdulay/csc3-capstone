#B.Booi
#vectors
# 22 april 2014
import math
def vectors():
    vecA = [0,0,0]
    vecB = [0,0,0]
    vecRes = [0,0,0]
    vecRes2 = [0,0,0]
    
    stringA = input("Enter vector A:\n")
    stringB = input("Enter vector B:\n")
    
    vecA = stringA.split(" ")
    vecB = stringB.split(" ")
    
    
    #Add
    for i in range(3):
        vecRes[i] = eval(vecA[i]) + eval(vecB[i])
    
    print("A+B = ",vecRes,sep ="")
    
    
    
    #multiply
    for x in range(3):
        vecRes[x] = eval(vecA[x])*eval(vecB[x])
    #print(vecRes)
        
    result = vecRes[0]+vecRes[1]+vecRes[2]
    print("A.B = ",result,sep ="")
    
    #NormA
    resultA = 0
    resultB = 0
    for yA in range(3):
        resultA =  resultA+ (eval(vecA[yA])**2)
     
    resultA =  round(math.sqrt(resultA) ,2)  
    
    if resultA == 0:
        print("|A| = 0.00")
    else:
        print("|A| = ",resultA,sep="")
    
    
    #NormB
    for yB in range(3):
        resultB =  resultB+ (eval(vecB[yB])**2)
        
    resultB =  round(math.sqrt(resultB) ,2)
    if resultB == 0:
        print("|B| = 0.00")
    else:
        print("|B| = ",resultB,sep="")    
    
    
    
    
    

vectors()
    
        