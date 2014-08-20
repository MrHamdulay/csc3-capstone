""" vector equations
barak setton
20/04/2014
"""
import math
vectorsum = []
vectorin = input("Enter vector A: \n") # creating the vectors
vectorpart = vectorin.split(" ")
vectorin = input("Enter vector B: \n") 
vectorpart2 = vectorin.split(" ")
vector = [[eval(vectorpart[0]),eval(vectorpart[1]),eval(vectorpart[2])],[eval(vectorpart2[0]),eval(vectorpart2[1]),eval(vectorpart2[2])]]

for col in range(3):
    vectorsum.append(vector[0][col]+ vector[1][col]) # adding the vectors
print ('A+B =',vectorsum)

vectordot = vector[0][0]*vector[1][0] + vector[0][1]*vector[1][1] + vector[0][2]*vector[1][2] # vector dotproduct
print("A.B =",vectordot)

vectormagA = math.sqrt((vector[0][0])**2 + (vector[0][1])**2 + (vector[0][2])**2) # magnitude of vector A
if vectormagA != 0:
    print("|A| =", round(vectormagA,2))
else:
    print("|A| = 0.00")
vectormagB = math.sqrt((vector[1][0])**2 + (vector[1][1])**2 + (vector[1][2])**2) # magnitude of vector B
if vectormagB != 0:
    print("|B| =", round(vectormagB,2))
else:
    print("|B| = 0.00")