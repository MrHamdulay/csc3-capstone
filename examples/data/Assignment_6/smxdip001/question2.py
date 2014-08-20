# a program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
#question2
#Author: Dipanjali Samoo
#Student Number: SMXDIP001
import math
d= input("Enter vector A: \n")
#create the list and evaluate the values
a= d.replace(" ",',')
array_A= a.split(",")
x= eval(array_A[0])
y= eval(array_A[1])
z= eval(array_A[2])

e= input("Enter vector B: \n")
#create the list and evaluate the values
l= e.replace(" ",',')
array_B= l.split(",")
A=eval(array_B[0])
B=eval(array_B[1])
C=eval(array_B[2])

#output printed
if x==0 and y==0 and z==0 and A==0 and B==0 and C==0:
    print("A+B = ",'[',(x+A),', ',(y+B),', ',(z+C),']',sep="")
    print("A.B = ",(x*A)+(y*B)+(z*C),sep="")
    print("|A| = ",'0.00',sep="")
    print("|B| = ",'0.00',sep="")
else:
    print("A+B = ",'[',(x+A),', ',(y+B),', ',(z+C),']',sep="")
    print("A.B = ",(x*A)+(y*B)+(z*C),sep="")
    print("|A| = ",round(math.sqrt(x**2+y**2+z**2),2),sep="")
    print("|B| = ",round(math.sqrt(A**2+B**2+C**2),2),sep="")
    