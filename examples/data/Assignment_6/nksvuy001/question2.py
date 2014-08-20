"""program to do basic vector calculations in 3 dimensions
vuyolwethu nkosi
23 april 2014"""

import math
#Get vector points from user
vector_A=input("Enter vector A:\n")
vector_A=vector_A.split() #split into strings
vector_B=input("Enter vector B:\n")
vector_B=vector_B.split()
#create empty list
A=[]
#make list
for i in vector_A:
    A.append(eval(i))
#create empty list    
B=[]
#make list B
for k in vector_B:
    B.append(eval(k))
#add every number in string A with every number in string B
x=A[0]+B[0]
y=A[1]+B[1]
z=A[2]+B[2]
#multiply every number in string A with every number in string B
x1=A[0]*B[0]
y2=A[1]*B[1]
z3=A[2]*B[2]
#every number in position squared
x11=A[0]**2
y22=A[1]**2
z33=A[2]**2
#every number in position squared
x111=B[0]**2
y222=B[1]**2
z333=B[2]**2
#print out results
print("A+B","=",[x,y,z])
print("A.B","=",(x1+y2+z3))
print("|A|","=","{0:.2f}".format((math.sqrt(x11+y22+z33))))
print("|B|","=","{0:.2f}".format((math.sqrt(x111+y222+z333))))