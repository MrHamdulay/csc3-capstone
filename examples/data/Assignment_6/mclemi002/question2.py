#emile mclennan
#assignment 6
#Q2

import math

vectA=input('Enter vector A:\n').split(" ")
vectB=input('Enter vector B:\n').split(" ")

a1 =eval(vectA[0]) #isolate values in array
a2= eval(vectA[1])
a3= eval(vectA[2])
b1= eval(vectB[0])
b2= eval(vectB[1])
b3= eval(vectB[2])
calc1 = [a1+b1, a2+b2, a3+b3]  #add items
calc2 = (a1*b1)+ (a2*b2)+ (a3*b3) #dot multiply
calc3 = round(math.sqrt((a1**2)+(a2**2)+(a3**2)),2) #normalise array 1
calc4 = round(math.sqrt((b1**2)+(b2**2)+(b3**2)),2) #normailse array 2
Y="|A| = {0:0.2f}".format(calc3)
Z="|B| = {0:0.2f}".format(calc4)

print('A+B =', calc1)
print('A.B =', calc2)
print(Y)
print(Z)
