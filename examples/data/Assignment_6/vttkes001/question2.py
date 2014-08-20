"""Vector Calculations in 3 Dimensions
Keshin Vittee
21 April 2014"""
import math

A = input("Enter vector A: \n").split(" ")
B = input("Enter vector B: \n").split(" ")

for i in range(3):
    A[i] = eval(A[i])
    B[i] = eval(B[i])
Add=[]

for i in range(3):
    Add += [A[i] + B[i]]

Mult = 0

for i in range(3):
    Mult+=A[i]*B[i]
    
#Normalization
sqsuma = 0
sqsumb = 0
for i in range(3):
    sqsuma += A[i]**2
    sqsumb += B[i]**2
    
sqsuma = math.sqrt(sqsuma)
sqsumb = math.sqrt(sqsumb)

print("A+B =",Add)
print("A.B =",Mult)
print("|A| =","{0:0.2f}".format(sqsuma))
print("|B| =","{0:0.2f}".format(sqsumb))





