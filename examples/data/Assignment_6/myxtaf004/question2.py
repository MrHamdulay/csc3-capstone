"""basic vector calculations 
Tafadzwa Moyo
21 April 2014"""
import math
#Gets vectors
a=input("Enter vector A:\n").split(" ")
b=input("Enter vector B:\n").split(" ")

#vector addition
vadd=[]
for i in range(3):
    a[i]=int(a[i])
    b[i]=int(b[i])
    vadd.append(a[i]+b[i])

#dot product
dpro=0
for i in range(3):
    dpro+=a[i]*b[i]
    
#normalization
anormsqd=0
bnormsqd=0
for i in range(3):
    anormsqd+=a[i]**2
for i in range(3):
    bnormsqd+=b[i]**2
anorm=round(math.sqrt(anormsqd), 2)
bnorm=round(math.sqrt(bnormsqd), 2)
if anorm==0:
    anorm="0.00"
if bnorm==0:
    bnorm="0.00"

#prints values
print("A+B =", vadd)
print("A.B =", dpro)
print("|A| =", anorm)
print("|B| =", bnorm)