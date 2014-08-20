"""Combining Vectors
Yamkela Venfolo
23 April 2014"""

import math
xString=input("Enter vector A:\n")
yString=input("Enter vector B:\n")

VectorA=xString.split(" ")
VectorB=yString.split(" ")

#Addition of Two vectors
Add=[]
for i in range(len(VectorA)):
    #add a new value to the array add
    Add.append(int(VectorA[i])+int(VectorB[i]))
print("A+B =",Add)  

#dot product
n=0
for i in range(len(VectorA)):
    n=n+(int(VectorA[i])*int(VectorB[i]))
print("A.B =",n) 

#|A| and |B|
sumA=0
sumB=0  
for i in range(len(VectorA)):
    sumA=sumA+((int(VectorA[i]))**2)
    sumB=sumB+((int(VectorB[i]))**2)
       
sumr=round(math.sqrt(sumA),2)
summ=round(math.sqrt(sumB),2)

print("|A| =","{0:.2f}".format(sumr))
print("|B| =","{0:.2f}".format(summ)) 
