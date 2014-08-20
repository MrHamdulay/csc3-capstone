import math

A1=input("Enter vector A:\n")
B1=input("Enter vector B:\n")

A=A1.split(" ")
B=B1.split(" ")

for i in range(3):
    A[i]=eval(A[i])
    B[i]=eval(B[i])

sum=[A[0]+B[0],A[1]+B[1],A[2]+B[2]]
print("A+B =",sum)

prod=A[0]*B[0]+A[1]*B[1]+A[2]*B[2]
print("A.B =",prod)

normA=math.sqrt(A[0]**2 + A[1]**2 + A[2]**2)
if normA==0:
    print("|A| = ",round(normA,1),"0",sep="")
else:
    print("|A| =",round(normA,2))

normB=math.sqrt(B[0]**2 + B[1]**2 + B[2]**2)
if normB==0:
    print("|B| = ",round(normB,1),0,sep="")
else:
    print("|B| =",round(normB,2))