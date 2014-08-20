'''Vector Products
Limpho Parkies
24-04-2014'''
import math
#variables
A=[]
B=[]
C=[]
D=0
E=0
G=0
A=input('Enter vector A:\n').split(" ")
B=input('Enter vector B:\n').split(" ")
#Calculations
for i in range(3):
    C.append(int(A[i])+int(B[i]))
print('A+B =',C)
for i in range(3):
    D+=int(A[i])*int(B[i])
print('A.B =',D)
for i in A:
    E+= eval(i)*eval(i)
    F=math.sqrt(E)
    z = "{0:.2f}".format(F)
print('|A| =',z)
for i in B:
    G+= eval(i)*eval(i)
    H=math.sqrt(G)
    k = "{0:.2f}".format(H)
print('|B| =',k)
