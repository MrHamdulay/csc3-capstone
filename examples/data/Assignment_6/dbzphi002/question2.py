#Thembekile Dubazana
#dbzphi002
#April 2014
#Assignment 6:Q2

"""Program for vector calculations"""
import math
#Enter the vectors
A=input("Enter vector A:\n")
B=input("Enter vector B:\n")
A=A.split()
B=B.split()

#Calculations
Addlist=[]
Dot=0
NormA=0
NormB=0
for i in range(3):
    Addlist.append(int(A[i]) + int(B[i]))#Addition
    Dot+=(int(A[i])*int(B[i]))#Dot
    NormA+=(int(A[i])**2)#Norm of A
    NormB+=(int(B[i])**2)#Norm of B
NormA=math.sqrt(NormA)
NormB=math.sqrt(NormB)


print('A+B =',Addlist)
print('A.B =',Dot)
print('|A| =',"{0:.2f}".format(NormA))
print('|B| =',"{0:.2f}".format(NormB))


      