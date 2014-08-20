#question2
# vector adition
#justin valsecchi
#2014/04/24

vectorA=[] #empty list A
vectorB=[] #empty list B
A=input("Enter vector A:\n") #getting values for list A
B=input("Enter vector B:\n") #getting values for list B
vectorA=A.split(" ") 
vectorB=B.split(" ")

for i in range(3):
    vectorA[i]=int(vectorA[i])
    vectorB[i]=int(vectorB[i])
A_plus_B = [vectorA[0]+vectorB[0], vectorA[1]+vectorB[1], vectorA[2]+vectorB[2]]
A_multi_B = vectorA[0]*vectorB[0]+vectorA[1]*vectorB[1]+vectorA[2]*vectorB[2]
normalizeA=(vectorA[0]**2+vectorA[1]**2+vectorA[2]**2)**(1/2)
normalizeB=(vectorB[0]**2+vectorB[1]**2+vectorB[2]**2)**(1/2)
print("A+B =", A_plus_B)
print("A.B =", A_multi_B)
print("|A| =", '{0:.2f}'.format(normalizeA))
print("|B| =", '{0:.2f}'.format(normalizeB))



    
    
