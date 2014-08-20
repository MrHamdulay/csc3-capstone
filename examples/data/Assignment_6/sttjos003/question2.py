#Program for Vectors
#Joe Sutton
#23 April 2014
import math

A = input("Enter vector A:\n")
A = A.split(" ") #turns A into a list

B = input("Enter vector B:\n")
B = B.split(" ")

sumAB=[] # create empty list

for i in range(3):
    newAB=eval(A[i])+eval(B[i])
    sumAB.append(newAB)

prodAB=0 #create new variable

for i in range(3):
    newprod=eval(A[i])*eval(B[i])
    prodAB+=newprod
    
funnyA=0 #create variable

for i in range(3):
    funnyA+=float(A[i])**2

funnyA=math.sqrt(funnyA)

funnyA=round(funnyA,2)

normA="{0:0<4}".format(funnyA)

funnyB=0 #create variable

for i in range(3):
    funnyB+=float(B[i])**2

funnyB=math.sqrt(funnyB)

funnyB=round(funnyB,2)
    
normB="{0:0<4}".format(funnyB)
    
print("A+B =", sumAB) 
print("A.B =", prodAB)
print("|A| =", normA)
print("|B| =", normB)