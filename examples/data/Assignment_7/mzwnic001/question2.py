#MZWNIC001/Nicholas Mazower    
#24/04/2014
#Basic vector operations calculator


import math
#This splits the input string into 3 seperate strings
vector_A=input("Enter vector A:\n").split(" ")
#This converts the input strings into integer x,y,z coordinates
x=eval(vector_A[0])
y=eval(vector_A[1])
z=eval(vector_A[2])

vector_A=[x,y,z]

vector_B=input("Enter vector B:\n").split(" ")
#i,j,k are valid coordinate names for vectors in place of x,y,z
i=eval(vector_B[0])
j=eval(vector_B[1])
k=eval(vector_B[2])

vector_B=[x,y,z]

addition=[x+i,y+j,z+k]
print("A+B =",addition)

dot_product=(x*i)+(y*j)+(z*k)
print("A.B =",dot_product)

norm_A=math.sqrt(x**2 + y**2 + z**2)
norm_A=round(norm_A,2)
norm_A=format(norm_A, '.2f') #The format is necessary to force the program to output 2 decimal zeroes
print("|A| =",norm_A)

norm_B=math.sqrt(i**2 + j**2 + k**2)
norm_B=round(norm_B,2)
norm_B=format(norm_B, '.2f')
print("|B| =",norm_B)
