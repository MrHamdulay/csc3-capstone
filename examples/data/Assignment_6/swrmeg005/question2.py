#A program that lets us do vector calculations in 3-D
#Megan Swartz
#24 April 2014

import math

#get the user to input a set of vectors 
vectorA = input("Enter vector A:\n")
vectorB = input("Enter vector B:\n")

vectorA = vectorA.split(" ")
vectorB = vectorB.split(" ")

#addition of the vectors:
sum_vector = []
for i in range(3):
    add = int(vectorA[i]) + int(vectorB[i])
    sum_vector.append(add)
    
print("A+B =", sum_vector)

#dot product 
dot_product = 0
for i in range(3):
    multiply = int(vectorA[i]) * int(vectorB[i])
    dot_product += multiply
    
print("A.B =", dot_product)

#normalization for a
norm_sum = 0
for i in range(3):
    square = int(vectorA[i]) ** 2
    norm_sum += square
norm = math.sqrt(norm_sum)
norm = "{0:.2f}".format(norm)
print("|A| =", norm)

#normalization for b
norm_sum = 0
for i in range(3):
    square = int(vectorB[i]) ** 2
    norm_sum += square
norm = math.sqrt(norm_sum)
norm = "{0:.2f}".format(norm)
print("|B| =", norm)
    
    