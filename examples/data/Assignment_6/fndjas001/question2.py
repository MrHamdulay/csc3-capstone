"""A program that does basic vector calculations in 3D
Jason Findlay
24/04/2014"""

import math

A=[]
B=[]
C=[]
d=0
e=0
f=0

A=input("Enter vector A:\n").split(" ")
B=input("Enter vector B:\n").split(" ")

#Make values stored in list integers
for i in range(3):
    A[i]=int(A[i])
    B[i]=int(B[i])
   
#Calculate and print A+B
for i in range(3):
    C.append(A[i]+B[i])
print("A+B =" ,C)

#Calculate A.B
for i in range(3):
    d+=A[i]*B[i]
print("A.B =", d)

#Calculate and print |A| and |B|
e=math.sqrt(((A[0])**2)+((A[1])**2)+((A[2])**2))
print("|A| = {0:.2f}".format(e))

f=math.sqrt(B[0]**2+B[1]**2+B[2]**2)
print("|B| = {0:.2f}".format(f))

