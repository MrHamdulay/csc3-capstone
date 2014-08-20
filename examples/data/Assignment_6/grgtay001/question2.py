"""Vector calculations in 3 dimensions program
Tayla George
23 April 2014"""

import math
#change vector(string) into list

listA=input("Enter vector A:\n")
A=listA.split() #splitting the vector into 3 values

listB=input("Enter vector B:\n")
B=listB.split() #splitting the vector into 3 values

#sum of vectors

sum_vector=[int(A[0])+int(B[0]),int(A[1])+int(B[1]),int(A[2])+int(B[2])]

print("A+B =",sum_vector)


#dot product

dotproduct=int(A[0])*int(B[0])+int(A[1])*int(B[1])+int(A[2])*int(B[2])
print("A.B =",dotproduct)

#norm vector A

a=math.sqrt(int(A[0])**2 +int(A[1])**2 +int(A[2])**2)
print("|A| =","{0:.2f}".format(a))  #format to 2 decimal places

#norm vector B

b=math.sqrt(int(B[0])**2 +int(B[1])**2 +int(B[2])**2)
print("|B| =","{0:.2f}".format(b))

