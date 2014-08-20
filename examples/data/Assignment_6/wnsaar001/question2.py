"""
vector program
Aaron Weinstein
21 April 2014
"""
import math
A=[]
B=[]
vecA=input("Enter vector A:\n")
vecB=input("Enter vector B:\n")
A=vecA.split(" ")
B=vecB.split(" ")

#print A[]+B[]
length=len(B)
a=0
b=0
c=0
a+=eval(A[0])+eval(B[0])
b+=eval(A[1])+eval(B[1])
c+=eval(A[2])+eval(B[2])
arr=[a,b,c]
print("A+B =",arr)
#print A[]*B[]
product=eval(A[0])*eval(B[0])+eval(A[1])*eval(B[1])+eval(A[2])*eval(B[2])
print("A.B = ", product, sep="")

#print|A|
#|A| = Sqrt(1^2 + 3^2 + 2^2) = Sqrt(1+9+4) = Sqrt(14) = 3.74

x=eval(A[0])
y=eval(A[1])
z=eval(A[2])
def absA(a, b, c):
    aa=(pow(a, 2)+pow(b,2)+pow(c,2))
    finA=round(math.sqrt(aa),2)
    if finA==0:
        print("|A| = 0.00")
    else:
        print("|A| = ", finA, sep="")
absA(x,y,z);

#print|B|
p=eval(B[0])
q=eval(B[1])
r=eval(B[2])
def absB(a, b, c):
    bb=(pow(a, 2)+pow(b,2)+pow(c,2))
    finB=round(math.sqrt(bb),2)
    if finB==0:
           print("|B| = 0.00")    
    else:
        print("|B| = ", finB, sep="")
absB(p,q,r);