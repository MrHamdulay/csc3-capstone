#Kalind Ramnarayan
#23 April 2014
#vector calculations

import math

vectorA=input("Enter vector A:\n")   #Create list for vector A
A=vectorA.split()
vectorB=input("Enter vector B:\n")   #Create list for vector B
B=vectorB.split()

AB=[eval(A[0])+eval(B[0]),eval(A[1])+eval(B[1]),eval(A[2])+eval(B[2])]  #Create new list according to the add vector manipulation
print("A+B = ",AB,sep="")

c=eval(A[0])*eval(B[0])+eval(A[1])*eval(B[1])+eval(A[2])*eval(B[2])   #vector manipulation 2
print("A.B = ",c,sep="")

normA="%.2f" % round(math.sqrt(eval(A[0])**2+eval(A[1])**2+(eval(A[2])**2)),2) #vector manipulation 3


print("|A| = ",normA,sep="")

normB="%.2f" % round(math.sqrt(eval(B[0])**2+eval(B[1])**2+(eval(B[2])**2)),2)

print("|B| = ",normB,sep="")
