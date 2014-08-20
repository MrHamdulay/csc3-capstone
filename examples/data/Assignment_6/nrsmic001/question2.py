"""Program to
Micaela Narasmulu
25 April 2014"""


import math 

vA= input("Enter vector A:\n") 

vB= input("Enter vector B:\n") 

va= vA.split()
vb= vB.split()

vS=[]#vectorsum

product=0
absA=0
absB=0

for i in  range (3):
    va[i]=eval(va[i]) 
    vb[i]=eval(vb[i])
    vS.append(va[i]+vb[i])
    product+=va[i]*vb[i]
    absA+=va[i]**2 
    absB+=vb[i]**2

print ("A+B =",vS)

print("A.B =",product) 

if (round(math.sqrt(absA),2))>0:
    print("|A| =",round(math.sqrt(absA),2))
else:
    print("|A| = 0.00")

if (round(math.sqrt(absB),2))>0:
    print("|B| =",round(math.sqrt(absB),2))
else:
    print("|B| = 0.00")

    