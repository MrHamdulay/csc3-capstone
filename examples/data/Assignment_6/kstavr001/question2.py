"""Assignment 6, Question 2
Avreyna Kistensamy
20 April 2014"""

import math

A = []
B = []

#creating array for user's A input
A_3 = input("Enter vector A:\n")
A_list = A_3.split(" ")
for num in A_list:
    A.append(num)
    
#creating array for user's B input
B_3 = input("Enter vector B:\n")
B_list = B_3.split(" ")
for num in B_list:
    B.append(num)
    
#Adding corresponding terms in lists
A_plus_B = []
for i in range(3):
    A_plus_B.append(eval(A[i]) + eval(B[i]))

#Multiplying corr. terms
A_B = []
for i in range(3):
    A_B.append(eval(A[i]) * eval(B[i]))
dot_p = A_B[0] + A_B[1] + A_B[2]

#norm of A
A_sq = []
for i in range(3):
    A_sq.append(eval(A[i])**2)
A_sq_sum = A_sq[0] + A_sq[1] + A_sq[2]  
A_rt= math.sqrt(A_sq_sum)

#norm of B
B_sq = []
for i in range(3):
    B_sq.append(eval(B[i])**2)
B_sq_sum = B_sq[0] + B_sq[1] + B_sq[2]  
B_rt= round(math.sqrt(B_sq_sum), 2)

#Printing vectors
print("A+B =", A_plus_B)
print("A.B =", dot_p)
print("|A| =", "{0:0.2f}".format(A_rt))
print("|B| =", "{0:0.2f}".format(B_rt))


    
