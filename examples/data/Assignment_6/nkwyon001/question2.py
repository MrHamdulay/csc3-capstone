"""program doing vector calculations
yondela nkwali
20 April 2014"""

import math
vA=input("Enter vector A:\n")
vA=vA.split(" ")
vB=input("Enter vector B:\n")
vB=vB.split(" ")
#addition
add1=eval(vA[0])+eval(vB[0])
add2=eval(vA[1])+eval(vB[1])
add3=eval(vA[2])+eval(vB[2])
addition=[add1,add2,add3]
#AaddB=", ".join(addition)

#dot product
AB=(eval(vA[0])*eval(vB[0]))+(eval(vA[1])*eval(vB[1]))+(eval(vA[2])*eval(vB[2]))

#normalization
A=round(math.sqrt((eval(vA[0]))**2+(eval(vA[1]))**2+(eval(vA[2]))**2),2)
B=round(math.sqrt((eval(vB[0]))**2+(eval(vB[1]))**2+(eval(vB[2]))**2),2)

#printing the values out
print("A+B =",addition)
print("A.B =",AB)
print("|A| =","%1.2f"% A)
print("|B| =","%1.2f"% B)

