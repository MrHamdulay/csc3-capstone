#Author: NLXALE001
#Date:23 April 2014
#Assignment 6

import math
#input vectors
a = input("Enter vector A:\n")
b = input("Enter vector B:\n")

#calculate A+B
aplusb=[]
a = a.split()
b = b.split()
for i in range (0, 3):
    temp = eval(a[i]) + eval(b[i])
    aplusb.append(str(temp))
printout = "[" + aplusb[0] + ", " + aplusb[1] + ", " + aplusb[2] + "]"
print ("A+B =", printout)

#calculate A.B
atimesb=0
for j in range (0, 3):
    temp = eval(a[j]) * eval(b[j])
    atimesb += temp
print ("A.B =", atimesb)

#calculate |A|
modA=0
for k in range (0, 3):
    temp = eval(a[k]) * eval(a[k])
    modA += temp
modA = math.sqrt(modA)
modA = round(modA, 2)
if len(str(modA))<4:
    modA = str(modA) + "0"
print ("|A| =", modA)

#calculate |B|
modB=0
for l in range (0, 3):
    temp = eval(b[l]) * eval(b[l])
    modB += temp
modB = math.sqrt(modB)
modB = round(modB, 2)
if len(str(modB))<4:
    modB = str(modB) + "0"
print ("|B| =", modB)
