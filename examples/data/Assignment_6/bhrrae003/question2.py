'''Program to do basic vector calculations 
Raeesa Behardien
BHRRAE003
Assignment 6
Question 2'''

A = []
B = []


import math
#to enter a list
vectorA = input("Enter vector A:\n")
A = vectorA.split()
vectorB = input("Enter vector B:\n")
B = vectorB.split()

#[A + B]
sum1 = (int(vectorA[0]) + int(vectorB[0]))
sum2 = (int(vectorA[2]) + int(vectorB[2]))
sum3 = (int(vectorA[4]) + int(vectorB[4]))
print("A+B = [",sum1,", ",sum2,", ",sum3,"]", sep="")

# (A.B)
dot1 = (int(vectorA[0]))*(int(vectorB[0]))
dot2 = (int(vectorA[2]))*(int(vectorB[2]))
dot3 = (int(vectorA[4]))*(int(vectorB[4]))
dot4 = dot1 + dot2 + dot3
print("A.B =", dot4)

#|A|
magA1 = int(vectorA[0])**2
magA2 = int(vectorA[2])**2
magA3 = int(vectorA[4])**2
sumA = math.sqrt(magA1 + magA2 + magA3)
print("|A| =","{0:.2f}".format(sumA))
            
#|B|
magB1 = int(vectorB[0])**2
magB2 = int(vectorB[2])**2
magB3 = int(vectorB[4])**2
sumB = math.sqrt(magB1 + magB2 + magB3)
print("|B| =","{0:.2f}".format(sumB))
