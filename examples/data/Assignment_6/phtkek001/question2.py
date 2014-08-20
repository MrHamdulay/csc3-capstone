"""Kekolo Phetla
PHTKEK001
Assignment 6
Question 2
21 April 2014"""

import math
#get input from user
vector_A=(input("Enter vector A:\n"))
vector_B=(input("Enter vector B:\n"))
#change input into list
vector_A=vector_A.split(" ")
vector_B=vector_B.split(" ")

#create variables
posA_0=int(vector_A[0])
posB_0=int(vector_B[0])
posA_1=int(vector_A[1])
posB_1=int(vector_B[1])
posA_2=int(vector_A[2])
posB_2=int(vector_B[2])

#addition    
sum1=posA_0+posB_0
sum2=posA_1+posB_1
sum3=posA_2+posB_2
sumtotal=[sum1,sum2,sum3]
print ("A+B =", sumtotal)

#dot product
prod1=posA_0*posB_0
prod2=posA_1*posB_1
prod3=posA_2*posB_2
dotproduct=prod1+prod2+prod3
print("A.B =", dotproduct)

#normalization of A
normA1=posA_0**2
normA2=posA_1**2
normA3=posA_2**2
normA=normA1+normA2+normA3
A=math.sqrt(normA)
print("|A| =", round(A,2))

#normalization of B
normB1=posB_0**2
normB2=posB_1**2
normB3=posB_2**2
normB=normB1+normB2+normB3
B=math.sqrt(normB)
print("|B| =", round(B,2))
    
    
    

