#question2
import math
print("Enter vector A:")
vect=input("")
vectorA=vect.split(" ")
print("Enter vector B:")
vect=input("")
vectorB=vect.split(" ")
vectorC=[eval(vectorA[0])+eval(vectorB[0]), eval(vectorA[1])+eval(vectorB[1]), eval(vectorA[2])+eval(vectorB[2])]
print("A+B =", vectorC) 
for i in range(len(vectorA)):
    vectorA[i]=eval(vectorA[i])
    vectorB[i]=eval(vectorB[i])
    
absA= round(math.sqrt(vectorA[0]**2 +vectorA[1]**2 +vectorA[2]**2),2)
absB= round(math.sqrt(vectorB[0]**2 + vectorB[1]**2 + vectorB[2]**2),2)
if absA==0:
    absA="0.00"
if absB==0:
    absB="0.00"

print("A.B =", vectorA[0]*vectorB[0] + vectorA[1]*vectorB[1] + vectorA[2]*vectorB[2])
print("|A| =", absA)
print("|B| =", absB)


    