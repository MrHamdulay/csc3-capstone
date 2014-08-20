"""ASSIGNMENT 6 QUESTION 2
Itumeleng Nqoko
24th April 2014"""
import math

A=input("Enter vector A:\n")
A1=A.split(" ")
B=input("Enter vector B:\n")
B1=B.split(" ")

addlis=[]
for i in range(3):
    add=int(A1[i])+int(B1[i])
    addlis.append(add)
print("A+B =",addlis)

prodadd=0
for i in range(3):
    prodadd+=int(A1[i])*int(B1[i])
    
print("A.B =",prodadd)

a=0
for i in range(3):
    a+=int(A1[i])*int(A1[i])
s=math.sqrt(a)
sq=round(s,2)
if s==0:
    print("|A| = 0.00")
else:
    print("|A| =",sq)
b=0
for i in range(3):
    b+=int(B1[i])*int(B1[i])
sq=math.sqrt(b)
squ=round(sq,2)
if sq==0:
    print("|B| = 0.00")
else:
    print("|B| =",squ)

