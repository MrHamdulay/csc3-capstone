'''SANELE MDLALOSE
   MDLSAN019
   Vectors: additional, dot products and normalization
   Assignment6,Question2
   21 April 2014'''
from math import *

A=input("Enter vector A:\n")  #Get vector values
A=A.split()
B=input("Enter vector B:\n")
B=B.split()

A_add_B=[' ', ' ', ' ']      #Create a list of three spaces
for i in range(len(A)):
    A_add_B[i] = int(A[i])+int(B[i])  #Change each space to a sum of corresponding integer items of vectors A and B
print("A+B =",A_add_B)      #Output Result

A_mult_B=[' ', ' ', ' ']   #Create a list of three spaces
for j in range(len(A)):
    A_mult_B[j] = int(A[j])*int(B[j])   #Change each space to a product of corresponding integer items of vectors A and B
    

for l in range(len(A_mult_B)):
    A_mult_B[l] = str(A_mult_B[l])   #Convert each item in A_mult_B list to a string
A_mult_B="+".join(A_mult_B)     #Join the string items by character "+"
print("A.B =",eval(A_mult_B))   #Evaluate the joined string into a number and output the result
 
norm_A=[' ', ' ', ' ']     #Create a list of three spaces
for a in range(len(A)):
    norm_A[a]= int(A[a])**2   #Change each space into a square of corresponding integer items in list A

for m in range(3):
    norm_A[m]=str(norm_A[m])   #Change each item in list norm_A into a string
norm_A="+".join(norm_A)      #Join the list of strings
norm_A=sqrt(eval(norm_A))   #Evaluate the resultant string into a square root number
if norm_A==0.0:
    norm_A='%.2f'%norm_A
    print("|A| =",norm_A)
else:
    print("|A| =", round(norm_A,2))  #Output a 2-decimal rounded answer

norm_B=[' ', ' ', ' ']    #Create a list of three spaces
for b in range (len(B)):
    norm_B[b] = int(B[b])**2  #Change each space into a square of integer items in list B  

for n in range (len(norm_B)):      
    norm_B[n] = str(norm_B[n])  #Convert each item in the list into a string
norm_B="+".join(norm_B)      #Join the string items
norm_B=sqrt(eval(norm_B))   #Evaluate the string into square root number
if norm_B==0.0:
    norm_B='%.2f'%norm_B
    print("|B| =",norm_B)

else:
    print("|B| =",round(norm_B,2))   #Output a 2-decimal-digit-rounded answer
