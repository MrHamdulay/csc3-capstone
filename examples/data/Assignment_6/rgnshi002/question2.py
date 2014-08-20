#Shivam Ragoonaden
#Vector calculation

import math

A = input("Enter vector A:\n")  #Get vectors from user
B = input("Enter vector B:\n")

Anums = []  #Initialise array
Bnums = [] 
ABsum = []
ABprod = 0
Anorm = 0
Bnorm = 0

for num in A.split():
    num = int(num)
    Anums.append(num)  #Put the 3 numbers into the array one by one
    
for num in B.split():
    num = int(num)
    Bnums.append(num)
    
for i in range(3):
    ABsum.append(Anums[i]  + Bnums[i])
    ABprod += Anums[i] * Bnums[i]
    Anorm += Anums[i]**2
    Bnorm += Bnums[i]**2
    
Anorm = str(round(Anorm**(1/2),2))
Bnorm = str(round(Bnorm**(1/2),2))

print("A+B =", ABsum) 
print("A.B =", ABprod)

if Anorm != "0.0":
    print("|A| =",Anorm)
else:
    print("|A| = 0.00")

if Bnorm != "0.0":
    print("|B| =",Bnorm)
else:
    print("|B| = 0.00")