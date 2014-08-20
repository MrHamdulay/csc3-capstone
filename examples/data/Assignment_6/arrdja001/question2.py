"""Assignment 6 Question 2
25 April 2014
Djavan Arrigone"""

import math #Allows for the use of python math library. 
A = input("Enter vector A: \n")
AA = A.split(" ")
VecA = [eval(AA[0]),eval(AA[1]),eval(AA[2])]

B = input("Enter vector B: \n")
BB = B.split(" ")
VecB = [eval(BB[0]),eval(BB[1]),eval(BB[2])]

def VectorAdd(VA,VB): #Adds the vectors together.
    
    VecAdd = [(VA[0] + VB[0]) , (VA[1] + VB[1]) , (VA[2] + VB[2])]
    return VecAdd

def VectorMult(VA,VB): #Multiply the vectors together.

    VecM = (VA[0] * VB[0]) + (VA[1] * VB[1]) + (VA[2] * VB[2])
    return VecM

def VectorAbsolute(V): #Calculate the absolute value of the vector

    VecAbs = math.sqrt((V[0]**2)+(V[1]**2)+(V[2]**2))
    VecAbs = "{:.2f}".format(VecAbs) #format which rounds answer to 2 decimal places.
    return VecAbs

print("A+B =", VectorAdd(VecA,VecB))
print("A.B =", VectorMult(VecA,VecB))
print("|A| =", VectorAbsolute(VecA))
print("|B| =", VectorAbsolute(VecB))
