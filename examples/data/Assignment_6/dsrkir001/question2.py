#Program to calaculate vector 
#20 April 2014
#Kiran Desraj

vectora = (input('Enter vector A:\n'))
a = ((vectora.split()))
a = list(map(int, a))       #Puts values of vector a in a list


vectorb = (input('Enter vector B:\n'))
b = ((vectorb.split()))
b = list(map(int, b))        #Puts values of vector b in a list      

import math    #to use square root function

#Calculate addition, dot product and normalization

c = [a[0]+b[0],a[1]+b[1],a[2]+b[2]]
d = (a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2])
e = (math.sqrt(((a[0]*a[0]) + (a[1]*a[1]) + (a[2]*a[2]))))
f = (math.sqrt(((b[0]*b[0]) + (b[1]*b[1]) + (b[2]*b[2]))))

#Print values accordingly

print("A+B =",c) 
print("A.B =",d)
if e ==0:
    print("|A| = 0.00")
else:
    print("|A| =",round(e, 2))
if f ==0: 
    print("|B| = 0.00")
else:
    print("|B| =",round(f, 2))