#NGMTAS001
#Question 2
#20 April 2014

def addition(vectorA, vectorB):
    newVector = []
    #appending values to the newvector
    for x in range(len(vectorA)):
        #converting them to integers
        newVector.append(int(vectorA[x])+int(vectorB[x]))
     
    print("A+B = [", end="")
    count = 0
    for i in newVector:
        #printing the structure
        if count != len(newVector) -1:
            print (i,", ",end="", sep="")
        else:
            print (i,end="")
        count = count+1
    print("]",end= "")    


def dotProduct(vectorA, vectorB):
    newVector = []
    #appending the newvector
    for x in range(len(vectorA)):
        newVector.append(int(vectorA[x])*int(vectorB[x]))
     
    print("A.B = ", end="")
    count = 0
    for i in newVector:
        count = count+i
       
    print(count)   




vecA = input ("Enter vector A:\n")
vectorA = vecA.split(" ")

vecB = input ("Enter vector B:\n")
vectorB = vecB.split(" ")

addition(vectorA, vectorB)
print()
dotProduct(vectorA,vectorB)

print("|A| = ", end ="")
total = 0.0
#summing up the second powers of compmonenets
for x in range(len(vectorA)):
    total = int(vectorA[x])**2 + total
    
if total ==0:
    print("0.00")
else: #working out the moduli     
    print (round((total**0.5),2))    
    
print("|B| = ", end ="")
total = 0.0

for x in range(len(vectorB)):
    total = int(vectorB[x])**2 + total
    
if total ==0:
    print("0.00")
else: #working out the moduli     
    print (round((total**0.5),2)) 