"""program to do vector calculations
Runako Muzwidzwa
23/04/2014"""
import math
vector_A=input("Enter vector A:\n")
vector_B=input("Enter vector B:\n")
A=vector_A.split()
B=vector_B.split()
#vector addition

x=int(A[0])+int(B[0])
y=int(A[1])+int(B[1])
z=int(A[2])+int(B[2])
add=[x,y,z]
print("A+B = ",add,sep="")

#vector multiplication
x1=int(A[0])*int(B[0])
y1=int(A[1])*int(B[1])
z1=int(A[2])*int(B[2])
product=(x1+y1+z1)
print("A.B =",product)

#norm of A
x2=(int(A[0]))**2
y2=(int(A[1]))**2
z2=(int(A[2]))**2
A_add=(x2+y2+z2)
norm_A=math.sqrt(A_add)
norm_Ar=round(norm_A,2)
if A_add==0:
    print("|A| = 0.00")
else:
    print("|A| =",norm_Ar)

#norm of B
x3=int(B[0])**2
y3=int(B[1])**2
z3=int(B[2])**2
B_add=(x3+y3+z3)
norm_B=math.sqrt(B_add)
norm_Br=round(norm_B,2)
if B_add==0:
    print("|B| = 0.00")
else:
    print("|B| =",norm_Br)
