"""Tofunmi Olagoke
OLGMOF001
23rd April 2014
Program to do basic vector calculations in 3 dimensions: addition, dot product and normalization."""

import math

A=input("Enter vector A:\n")
B=input("Enter vector B:\n")

listA=A.split(" ")
listB=B.split(" ")

#A+B
C=[(eval(listA[0])+eval(listB[0])),(eval(listA[1])+eval(listB[1])),(eval(listA[2])+eval(listB[2]))]
#A*B
D=(eval(listA[0])*eval(listB[0]))+(eval(listA[1])*eval(listB[1]))+(eval(listA[2])*eval(listB[2]))
#|A|
E=(eval(listA[0])**2)+(eval(listA[1])**2)+(eval(listA[2])**2)
#|B|
F=(eval(listB[0])**2)+(eval(listB[1])**2)+(eval(listB[2])**2)

print("A+B =",C)
print("A.B =",D)
print("|A| =",'{:.2f}'.format(math.sqrt(E)))
print("|B| =",'{:.2f}'.format(math.sqrt(F)))