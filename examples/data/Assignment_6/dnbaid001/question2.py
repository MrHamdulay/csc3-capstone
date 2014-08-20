#Assignment 6 - Question 2
#Basic vector calculations
#Author: Aidan de Nobrega DNBAID001
#19/04/2014

from math import sqrt

Ainput = input("Enter vector A:\n")
Binput = input("Enter vector B:\n")

A = Ainput.split() #converts Ainput to a list of strings
A = [int(x) for x in A] #Makes each element in list an int
B = Binput.split()
B = [int(x) for x in B]

addition_list = [A[0]+B[0], A[1]+B[1], A[2]+B[2]]
dot_product_string = A[0]*B[0] + A[1]*B[1] + A[2]*B[2]
absolute_A = round(sqrt(A[0]**2 + A[1]**2 + A[2]**2), 2) #round to 2 decimals
absolute_B = round(sqrt(B[0]**2 + B[1]**2 + B[2]**2), 2)


print("A+B = " + str(addition_list))
print("A.B = " + str(dot_product_string))
print("|A| = " + "{0:.2f}".format(absolute_A)) #string formatting shows 2 decimals even when 0
print("|B| = " + "{0:.2f}".format(absolute_B))