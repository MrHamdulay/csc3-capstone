#kairav soni
import math

VecA=input("Enter vector A:\n")
A=VecA.split(" ")
VecB=input("Enter vector B:\n")
B=VecB.split(" ")

x=[]
for i in range(len(A)):
    y=eval(A[i])+eval(B[i])
    x.append(y)  
print("A+B = ", x, sep="")

z=0
for j in range(len(A)):
    mult= eval(A[j])*eval(B[j])
    z=z+mult
print("A.B = ", z, sep ="")

a=0
for l in range(len(A)):
    mult1=eval(A[l])**2
    a=a+mult1
    
root=math.sqrt(a)
root=str(root)
sroot=root.split(".")
splroot=sroot[1][0:2]


if eval(splroot)!=0:
    splroot=round(eval(root),2)
    print("|A| = " + str(splroot))
    
    
    
else:
    allign="{0:0<2}"
    print("|A| = " + sroot[0] + "." + allign.format(splroot))
    
    

b=0
for k in range(len(B)):
    root1=eval(B[k])**2
    b=b+root1
    
root2=math.sqrt(b)
root2=str(root2)
splroot1=root2.split(".")
iroot1=splroot1[1][0:2]

if eval(iroot1)!=0:
    iroot1=round(eval(root2),2)
    print("|B| = " + str(iroot1))
    
    

else:
    allign1="{0:0<2}"
    print("|B| = " + splroot1[0] + "." + allign1.format(iroot1))
