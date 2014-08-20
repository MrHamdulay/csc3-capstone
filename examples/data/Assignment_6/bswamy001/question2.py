""" Amy Bosworth, Assignment 6, question 2, program to do basic vector calculations"""

import math

# Get inputs
A=input("Enter vector A:\n")
B=input("Enter vector B:\n")

# Store vectors as strings
vectorsA= A.split()
vectorsB= B.split()

# Addition
addition=[]
for i in range(len(vectorsA)):
    ans= eval(vectorsA[i]) + eval(vectorsB[i])
    addition.append(ans)
print("A+B =",addition)
    
# dot product
final_ans= 0
for i in range(len(vectorsA)):
    ans= eval(vectorsA[i]) * eval(vectorsB[i])
    final_ans+=ans
    
print("A.B =",final_ans)

# normalization vector A
final_ans= 0
for i in vectorsA:
    ans=eval(i)**2
    final_ans+=ans
    
final_ans=math.sqrt(final_ans)
final_ans="{0:.2f}".format(final_ans) #round to 2 decimal places

print("|A| =",final_ans)

# normalization vector B
final_ans=0
for i in vectorsB:
    ans=eval(i)**2
    final_ans+=ans
    
final_ans=math.sqrt(final_ans)
final_ans="{0:.2f}".format(final_ans) #round to 2 decimal places

print("|B| =",final_ans)



    
    
    



