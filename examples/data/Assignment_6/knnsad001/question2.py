#Program to calaculate vectors 
#KNNSAD001
#question2
 
#introducing variables: 

vectorA = (input('Enter vector A:\n'))
b = ((vectorA.split()))
b = list(map(int, b))       

 #this puts the values of vector a in list form


vectorB = (input('Enter vector B:\n'))
c = ((vectorB.split()))
c = list(map(int, c))        

#this puts the values of vector b in list form      

import math    # this will enable us to use square root function in math library

#this will calculate the addition, dot product and the normalization

d = [b[0]+c[0],b[1]+c[1],b[2]+c[2]]
e = (b[0]*c[0]) + (b[1]*c[1]) + (b[2]*c[2])
f = (math.sqrt(((b[0]*b[0]) + (b[1]*b[1]) + (b[2]*b[2]))))
g = (math.sqrt(((c[0]*c[0]) + (c[1]*c[1]) + (c[2]*c[2]))))

#to print values calculated,respectively

print("A+B =",d) 
print("A.B =",e)
if f ==0:
    print("|A| = 0.00")
else:
    print("|A| =",round(f, 2))
if g ==0: 
    print("|B| = 0.00")
else:
    print("|B| =",round(g, 2))