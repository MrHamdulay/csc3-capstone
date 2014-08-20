''' Program to do basic vector calculations in 3 dimensions
21 April 2014
Matshepo Malatjji'''

import math

#Receive vectors from user and add to lists
A = input("Enter vector A:\n").split(' ')
B = input("Enter vector B:\n").split(' ')

#Addition
sum = []
for i in range(3):
    sum.append(int(A[i]) + int(B[i]))
print('A+B = ', end ='')
print(sum)

#Dot product
product = 0
for j in range(3):
    product += int(A[j]) * int(B[j])
print('A.B = ' + str(product))

#Normalizatin
totalsquare = 0
for k in range(3):
    totalsquare +=  int(A[k])**2  
normA = math.sqrt(totalsquare)
output = '|A| = {0:0.2f}'
print(output.format(normA))

totalsquare = 0
for m in range(3):
    totalsquare +=  int(B[m])**2  
normB = math.sqrt(totalsquare)
output = '|B| = {0:0.2f}'
print(output.format(normB))