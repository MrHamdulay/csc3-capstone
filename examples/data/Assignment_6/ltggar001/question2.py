'''Program to deal with sets of vectors in ways to do things and stuff also
Gareth Lategan
25-04-2014'''

import math

inputA = input("Enter vector A:\n")
inputB = input("Enter vector B:\n")
veca=inputA.split(" ") #Turn the input into an array of 3
vecb=inputB.split(" ")
A=[eval(veca[0]),eval(veca[1]),eval(veca[2])] #Convert the strings into integers
B=[eval(vecb[0]),eval(vecb[1]),eval(vecb[2])]

#addition of corresponding elements
AplusB = []
for i in range(3):
    AplusB.append(A[i]+B[i])
print("A+B =",AplusB)

#sum of products of corresponding elements

AB = (A[0]*B[0])+(A[1]*B[1])+(A[2]*B[2])
print("A.B =",AB)

#norm of vectors
if A == [0,0,0]:
    print("|A| = 0.00")
else:
    print("|A| =",round(math.sqrt((A[0]**2)+(A[1]**2)+(A[2]**2)),2))
if B == [0,0,0]:    
    print("|B| = 0.00")
else:
    print("|B| =",round(math.sqrt((B[0]**2)+(B[1]**2)+(B[2]**2)),2))