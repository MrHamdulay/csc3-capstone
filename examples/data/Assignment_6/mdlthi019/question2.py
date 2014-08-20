"""Program to calculate vectors
Thiloshni Moodley
22 April 2014"""

import math

A = input("Enter vector A:\n")
B = input("Enter vector B:\n")

A= A.split(' ')
B= B.split(' ')

#Addition
A_plus_B = [] #empty list
A_plus_B.append(eval(A[0])+eval(B[0])) #adding each corresponding vector
A_plus_B.append(eval(A[1])+eval(B[1]))
A_plus_B.append(eval(A[2])+eval(B[2]))

#Multiplication
A_multiply_B = (eval(A[0])*eval(B[0]))+(eval(A[1])*eval(B[1]))+(eval(A[2])*eval(B[2])) #sum of all values multiplied

#Norm
norm_A = (math.sqrt(eval(A[0])**2+ eval(A[1])**2 + eval(A[2])**2)) #calculate norm
deci_norm_A = "{0:0.2f}".format(norm_A) # correct decimal value
norm_B = (math.sqrt(eval(B[0])**2+ eval(B[1])**2 + eval(B[2])**2)) #calculate norm
deci_norm_B = "{0:0.2f}".format(norm_B) # correct decimal value

#Output
print('A+B =', A_plus_B)
print('A.B =', A_multiply_B)
print('|A| =', deci_norm_A)
print('|B| =', deci_norm_B)
