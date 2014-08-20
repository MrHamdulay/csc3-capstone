# program to do vector calculations in 3 dimensions
# hendrik joosten
# 24/04/2014

# import math.py to use math.sqrt()
import math

#populate the vectors A and B
vectorA = input("Enter vector A:\n")
vectorA = vectorA.split()
vectorB = input("Enter vector B:\n")
vectorB = vectorB.split()

# declare empty array to store the answer of addition
answer = []

# add the elements of the vectors and store them in array answer
for i in range(len(vectorA)):
      answer.append(eval(vectorA[i])+eval(vectorB[i]))
print("A+B =", answer)

# declare the answer of multiplcation
dotMultiply = 0

# do the multiplcaion of all elements
for j in range(len(vectorA)):
      dotMultiply = dotMultiply + (eval(vectorA[j])*eval(vectorB[j]))
print("A.B =", dotMultiply)


# declare answers for last calculation 
A = 0
B = 0

# do the calcution for vector A
for x in range(len(vectorA)):
      A = A + eval(vectorA[x])**2
A = math.sqrt(A)

# do the calcution for vector B
for y in range(len(vectorB)):
      B = B + eval(vectorB[y])**2
B = math.sqrt(B)

# print the answers
print("|A| =", "{0:0.2f}".format(round(A,2)))
print("|B| =", "{0:0.2f}".format(round(B,2)))




      

