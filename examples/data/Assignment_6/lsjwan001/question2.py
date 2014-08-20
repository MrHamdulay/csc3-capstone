# Program to do baisc vector calculationsin 3 dimensions
# Wandile Lesejane
# 20 April 2014

import math
# enter vectors and evaluate thier components
vectA=input("Enter vector A:\n")
A=vectA.split(" ")
a1=eval(A[0])
a2=eval(A[1])
a3=eval(A[2])

vectB=input("Enter vector B:\n")
B=vectB.split(" ")
b1=eval(B[0])
b2=eval(B[1])
b3=eval(B[2])

# vector addition
add=[a1+b1,a2+b2,a3+b3]
print("A+B =",add)
# vector multiplication
mult=a1*b1+a2*b2+a3*b3
print("A.B =",mult)

#magnitude of vectors
absA=math.sqrt(a1**2+a2**2+a3**2)
print("|A| =",'{0:0.2f}'.format(absA))
absB=math.sqrt(b1**2+b2**2+b3**2)
print("|B| =",'{0:0.2f}'.format(absB))
