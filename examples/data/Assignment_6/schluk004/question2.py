import math

vecA=input("Enter vector A:\n").split()
vecA = list(map(int,vecA))

vecB=input("Enter vector B:\n").split()
vecB = list(map(int,vecB))

def add(vecA,vecB):
    addlist=[]
    for i in range(3):
        addlist.append(vecA[i]+vecB[i])
    return(addlist)

def dprod(vecA,vecB):
    dp=0
    for i in range(3):
        dp+=vecA[i]*vecB[i]
    return(dp)

def norm(vec):
    total=0
    for i in range(3):
        total+=vec[i]**2
    return(math.sqrt(total))

print("A+B =",add(vecA, vecB))
print("A.B =",dprod(vecA, vecB))
print("|A| =","{:.2f}".format(norm(vecA)))
print("|B| =","{:.2f}".format(norm(vecB)))
    
 
        
    
        