"""Vector calculations in 3 dimensions
Paul Truter
22 April 2014"""

import math

#Get vectors for A
a_string = input("Enter vector A:\n")
A = a_string.split(" ")

#Get vectors for B
b_string = input("Enter vector B:\n")
B = b_string.split(" ")

#calculate values
sum_of_ab = [int(A[0])+int(B[0]),int(A[1])+int(B[1]), int(A[2])+int(B[2])]
print("A+B =",sum_of_ab)

dot_product = int(A[0])*int(B[0])+int(A[1])*int(B[1])+int(A[2])*int(B[2])
print("A.B =",dot_product)

square_root_A = '{0:0.2f}'.format((math.sqrt(int(A[0])*int(A[0]) + int(A[1])*int(A[1]) + int(A[2])*int(A[2]))))
print("|A| =",square_root_A)

square_root_B = '{0:0.2f}'.format((math.sqrt(int(B[0])*int(B[0]) + int(B[1])*int(B[1]) + int(B[2])*int(B[2]))))
print("|B| =",square_root_B)