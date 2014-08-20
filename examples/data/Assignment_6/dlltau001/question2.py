#Question 2
#Assignment 6
#Tauriq Dolley

#Input Vectors

import math 

vect_A = []
vect_B = []
norm_A = []
norm_B = []
addition = []
sum = []

vect_A = input("Enter vector A:\n").split()
vect_B = input("Enter vector B:\n").split()


for i in range(len(vect_A)):
    addition.append(eval(vect_A[i]) + eval(vect_B[i]))
print("A+B =",addition) 


for i in range(len(vect_A)):
    sum.append(eval(vect_A[i])*eval(vect_B[i]))
dot = sum[0]+sum[1]+sum[2]
print("A.B =",dot)


for i in range(len(vect_A)):
    norm_A.append(eval(vect_A[i])**2)
total_A = norm_A[0]+ norm_A[1]+ norm_A[2]
squareroot_A = "{0:2.2f}".format(math.sqrt(total_A),2)
print("|A| =",squareroot_A)


for i in range(len(vect_B)):
    norm_B.append(eval(vect_B[i])**2)
total_B = norm_B[0]+ norm_B[1]+ norm_B[2]
squareroot_B = "{0:2.2f}".format(math.sqrt(total_B))
print("|B| =",squareroot_B)