# Michaela Heale
# Assignment 6 Question 2
# Vectors
import math

# gets data from user
A = []
B = []

Aopt = input ("Enter vector A:\n")
optA = Aopt.strip()
A = optA.split(" ")

Bopt = input ("Enter vector B:\n")
optB = Bopt.strip()
B = Bopt.split(" ")

#creates a count variable
cA = len(A)
cB = len(B)
c = 0
if (cA == cB):
    c = cB

# Finds the sum of A and B vectors

ABadd = []
for x in range(0,c):
    sum = eval(A[x]) + eval(B[x])
    ABadd.append(sum)
print("A+B = [",ABadd[0],", ",ABadd[1],", ",ABadd[2],"]",sep="")

# Works out the dot product of A and B vectors
dot = 0
for e in range(0,c):
    prod = eval(A[e])*eval(B[e])
    dot += prod
print("A.B =",dot)

# Normalises the A and B vectors

absA = 0
absB = 0
for w in range(0,c):
    sqrtA = math.pow(eval(A[w]),2)
    sqrtB = math.pow(eval(B[w]),2)
    absA += sqrtA
    absB += sqrtB   
if not (absA == 0 and absB == 0):
    print("|A| =",round(math.sqrt(absA),2))
    print("|B| =",round(math.sqrt(absB),2))
else:
    print("|A| = 0.00")
    print("|B| = 0.00")    