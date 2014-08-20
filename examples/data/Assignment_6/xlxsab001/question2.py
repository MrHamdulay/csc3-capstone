import math

vectA = input("Enter vector A:\n")
newvectA= vectA.split(' ')
vectB = input("Enter vector B:\n")
newvectB=vectB.split(' ')


A=[int(i) for i in newvectA]
B=[int(i) for i in newvectB]

AplusB = [(A[0]+B[0]), (A[1]+B[1]), (A[2]+B[2])]
#AplusB=A+B
AtimesB= (A[0]*B[0]+ A[1]*B[1]+ A[2]*B[2])
absA= (math.sqrt(A[0]**2+A[1]**2+A[2]**2))
absB= (math.sqrt(B[0]**2+B[1]**2+B[2]**2))
print("A+B =",AplusB)
print("A.B =",AtimesB)

if A!=[0,0,0] and B!=[0,0,0]:  
    print("|A| =",round(absA, 2))
    print("|B| =",round(absB, 2))

elif A ==[0,0,0] and B == [0,0,0]:
    print("|A| = 0.00")
    print("|B| = 0.00")