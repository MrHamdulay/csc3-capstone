#calculating dot and cross products of input
#wayne de jager
#23 april 2014

import math
#creat list from input
vecA=input("Enter vector A:\n")
a=vecA.split(" ")
vecB=input("Enter vector B:\n")
b=vecB.split(" ")
#vector sum
vecsum=[]
for i in range(3):
    z=eval(a[i])+eval(b[i])
    vecsum.append(z)
print("A+B =",vecsum)
#dot product
dot=[]
for i in range(3):
    z=eval(a[i])*eval(b[i])
    dot.append(z)
    dotprod=sum(dot)
print("A.B =",dotprod)
#vectorA
IofA=eval(a[0])**2
JofA=eval(a[1])**2
KofA=eval(a[2])**2
vectorA=round(math.sqrt(IofA+JofA+KofA),2)
if vectorA==0:
    print("|A| =","0.00")
else: print("|A| =",vectorA)
#print("|A| =",vectorA)
#vectorB
IofB=eval(b[0])**2
JofB=eval(b[1])**2
KofB=eval(b[2])**2
vectorB=round(math.sqrt(IofB+JofB+KofB),2)
if vectorB==0:
    print("|B| =","0.00")
else: print("|B| =",vectorB)
#print("|B| =",vectorB)