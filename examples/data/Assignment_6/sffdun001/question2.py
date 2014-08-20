"""Assignment 6- Question 2: Basic Vector calculations
Duncan Saffy
April 20 2014"""

import math

A=input("Enter vector A:\n")
B=input("Enter vector B:\n")
A=A.split(" ")
B=B.split(" ")
add=[]
a=[]
b=[]
multiply=0
for i in range(3):
    strA=eval(A[i])
    strB=eval(B[i])
    a.append(strA)
    b.append(strB)
    
for j in range(3):
    summ=a[j]+b[j]
    add.append(summ)
    product=a[j]*b[j]
    rtA=round(math.sqrt((a[0]**2)+(a[1]**2)+(a[2]**2)),2)
    rtB=round(math.sqrt((b[0]**2)+(b[1]**2)+(b[2]**2)),2)
    #rta=rtA.format(::.00)
    #rtb=rtB.format(::.00)
    multiply+=product
Y="|A| = {0:0.2f}".format(rtA)
Z="|B| = {0:0.2f}".format(rtB)
    
print("A+B =",add)
print("A.B =",multiply)
#print("|A| =",{0:0.2}.format(rtA))
#print("|B| =",{0:0.2}.format(rtB))
print(Y)
print(Z)