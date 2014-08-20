"""These program do the basic vector calculations in 3 dimensions
Masilela Mduduzi
24 April 2014"""
import math #to be able to calculate the square root later

vectorA = input("Enter vector A:\n") #requeting vector A from the user
vectorB = input("Enter vector B:\n") #requesting vector B

A=vectorA.split(' ') #split string(vectorA) into a list
B=vectorB.split(' ') #split string(vectorB) into a list

A_B = [eval(A[0]) + eval(B[0]), eval(A[1]) + eval(B[1]), eval(A[2])+eval(B[2])]
print("A+B =",A_B)

AB =  eval(A[0]) * eval(B[0])+ eval(A[1]) * eval(B[1])+ eval(A[2])*eval(B[2])
print("A.B =",AB)

normA = math.sqrt(eval(A[0])**2+eval(A[1])**2+eval(A[2])**2)
print("|A| = {0:0.2f}".format(normA,2))

normB = math.sqrt((eval(B[0])**2+eval(B[1])**2+eval(B[2])**2))
print("|B| = {0:0.2f}".format(normB,2))
