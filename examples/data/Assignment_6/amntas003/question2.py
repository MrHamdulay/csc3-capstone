#AMNTAS003  #Tashfia Amin   #Due date: 25 April 2014
#Question 2: Assignment 6   #Vector Calculations

import math

#Create a 2D array from the input of 2 vectors
A = input("Enter vector A: \n")
vectorA=A.split(" ")
B = input("Enter vector B: \n")
vectorB=B.split(" ")

#Print the addition of the two vector values
addition=[]
for i in range(3):
    addition.append(eval(vectorA[i]) + eval(vectorB[i]))
print("A+B =", addition)

#Print the multiplication of the two vectors
multiply=0
for i in range(3):
    x=eval(vectorA[i]) * eval(vectorB[i])
    multiply=multiply+x
print("A.B =", multiply)

#Norm of vectors for A
norm_a=0
for i in range(3):
    x=(eval(vectorA[i]))**2
    norm_a=norm_a+x
print("|A| =", "{0:0<4}".format(round(math.sqrt(norm_a), 2)))

#Norm of vectors for B
norm_b=0
for i in range(3):
    x=eval(vectorB[i])**2
    norm_b=norm_b+x
print("|B| =", "{0:0<4}".format(round(math.sqrt(norm_b), 2)))