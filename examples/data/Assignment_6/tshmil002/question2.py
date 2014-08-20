'''Addition, multiplication and squaring of vectors
Inga Ndyoki
24 April 2014'''
import math
A = (input('Enter vector A:\n')).split(" ")
B = (input('Enter vector B:\n')).split(" ")
add = []

for i in range(len(A)):                #Adding the two vectoers
    add.append(eval(A[i])+eval(B[i]))

multi = 0

for i in range(len(A)):                #dot multiplication
    multi += (eval(A[i])*eval(B[i]))

Anorm, Bnorm = 0.0,0.0

for i in range(len(A)):                #normalization of A and B
    Anorm += (math.pow(eval(A[i]),2))
    Bnorm += (math.pow(eval(B[i]),2))

print("A+B =",add)
print("A.B =",multi)
print("|A| =",("%0.2f")%(math.sqrt(Anorm)))
print("|B| =",("%0.2f")%(math.sqrt(Bnorm)))