'''Vector calculations in 3-D
Author:Raees Eland
Date:20 April 2014'''

import math
VectorA=input('Enter vector A:\n')
VectorB=input('Enter vector B:\n')
VectorA=VectorA.split(' ')
VectorB=VectorB.split(' ')

#Vector addition
x=0
add=[]
for i in range(3):
    add.append(eval(VectorA[x])+eval(VectorB[x]))
    x+=1
print('A+B =',add)

#Dot product
dot=[]
x=0
A_dot_B=0
for j in range(3):
    dot.append(eval(VectorA[x])*eval(VectorB[x]))
    A_dot_B+=dot[x]
    x+=1
print('A.B =',A_dot_B)

Ax,Ay,Az=eval(VectorA[0]),eval(VectorA[1]),eval(VectorA[2])
normA=float(math.sqrt((Ax*Ax)+(Ay*Ay)+(Az*Az)))
if normA==0:
    print('|A| =','0.00')
else:
    print('|A| =',round(normA,2))

Bx,By,Bz=eval(VectorB[0]),eval(VectorB[1]),eval(VectorB[2])
normB=float(math.sqrt((Bx*Bx)+(By*By)+(Bz*Bz)))
if normB==0:
    print('|B| =','0.00')
else:
    print('|B| =',round(normB,2))




    
    