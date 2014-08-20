#question 2
#Tendani Netshitenzhe
#25 April 2014

from math import *

#Obtain the values of the vectors
A = input("Enter vector A:\n").split()
B = input("Enter vector B:\n").split()

#Create empty vector lists
vectorA = []
vectorB = []

#Add entered values into respective lists
vectorA.append(A)
vectorB.append(B)

addition = []
dot_product = 0
norm_A = 0
norm_B = 0

for i in range(3):
    addition.append(int(vectorA[0][i])+int(vectorB[0][i])) #Adding vectors
    dot_product += int(vectorA[0][i])*int(vectorB[0][i]) #Dot product of vectors
    norm_A += int(vectorA[0][i])**2 #normalization of vector A
    norm_B += int(vectorB[0][i])**2 #normalization of vector B

#Display addition, dotproduct and normalisation of vector A and B    
print("A+B =", addition)
print("A.B =", dot_product)
print("|A| =", ("%.2f" % sqrt(norm_A)))
print("|B| =", ("%.2f" % sqrt(norm_B)))