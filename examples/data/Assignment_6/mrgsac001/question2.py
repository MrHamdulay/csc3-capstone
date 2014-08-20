"""Vectors
Sachin Murugan 
24/04/2014"""
import math #in order to use sqrt function in normalisation
Vector1=input("Enter vector A:\n")
VectorA = []
for i in Vector1.split(): #converts the string into integers
    VectorA.append(int(i))

Vector2 =input("Enter vector B:\n")
VectorB = []
for i in Vector2.split():
    VectorB.append(int(i))

Vector_Addition = []
for i in range (0,len(VectorA)):
    Vector_Addition.append(VectorA[i] + VectorB[i])
print ("A+B =", Vector_Addition)

Vector_Dot_Product = []
for i in range(0,len(VectorA)):
    Vector_Dot_Product.append(VectorA[i]*VectorB[i]) 
Sum_Product = sum(Vector_Dot_Product)

print ("A.B =", Sum_Product)

Vector_NormA = []
for i in range(0,len(VectorA)):
    Vector_NormA.append(i**2)
Sum_NormA = sum(Vector_NormA)
sqrtA = math.sqrt(Sum_NormA)
A = "{0:.2f}".format(sqrtA)
print ("|A| =", sqrtA)

Vector_NormB = []
for i in range(0,len(VectorB)):
    Vector_NormB.append(i**2)
Sum_NormB= sum(Vector_NormB)
sqrtB = math.sqrt(Sum_NormB)
B = "{0:.2f}".format(sqrtB)
print ("|B| =",B)