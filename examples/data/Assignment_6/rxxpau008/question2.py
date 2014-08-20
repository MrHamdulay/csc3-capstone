#Description: Vecor Calculations of 2 vectors, A and B
#Name: Paul Roux - RXXPAU008
#Date: 22 April 2014

import math

vector_A = (input('Enter vector A:\n')).split()

vector_B = (input('Enter vector B:\n')).split()
 
for i in range(0,3): #Converts the first 3 entries from strings
    vector_A[i] = eval(vector_A[i])
    vector_B[i] = eval(vector_B[i])

print('A+B = ',end='')
A_plus_B = []
for i in range(0,3): #Calculates an element in A plus the same element in B
    A_plus_B.append(vector_A[i]+vector_B[i])
print(A_plus_B)

print('A.B = ',end='')
A_dot_B = 0
for i in range(0,3): #Calculates the dot product of A and B
    A_dot_B+= vector_A[i]*vector_B[i]
print(A_dot_B)

print('|A| = ',end='')
normalization_A = round(math.sqrt(vector_A[0]**2+vector_A[1]**2+vector_A[2]**2),2)
print("%.2f" %normalization_A) #Prints the normalization of A to 2 decimal places

print('|B| = ',end='')
normalization_B = round(math.sqrt(vector_B[0]**2+vector_B[1]**2+vector_B[2]**2),2)
print("%.2f" %normalization_B) #Prints the normalization of B to 2 decimal points