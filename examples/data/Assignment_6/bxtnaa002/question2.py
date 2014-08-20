# question2.py
# author: bxtnaa002
 
import math
A_str = input("Enter vector A:\n") #input of the different vectors
B_str = input("Enter vector B:\n")

A = A_str.split(" ")
B = B_str.split(" ")

add = [] # create a list for the sums of the items in the different vectors
for i in range(len(A)): #go through each item in the vectors
    add.append(int(A[i]) + int(B[i])) #make item a number in order to add
print("A+B = "+ str(add))

multiply = 0
for l in range(len(A)):
    d = (int(A[l]) * int(B[l]))
    multiply += d #finds the total of the products
    
print("A.B = "+ str(multiply))
    
normalA = 0
for k in range(len(A)):
    a = (int(A[k])**2) #exponentiation
    normalA += a
norA = math.sqrt(normalA)
print("|A| = "+"{0:.2f}".format(norA)) #produce answer to 2 decimal places

normalB = 0
for j in range(len(B)):
    b = (int(B[j])**2)
    normalB += b
norB = math.sqrt(normalB)
print("|B| = "+"{0:.2f}".format(norB))
