""""the program that calculates the addition of vectors,
dot product and norm of a single vector
By Bruce Sontshoto
20 April 2014 """

import math
#asking for an input of vector A from the user    
vectorA = []
vecA = input("Enter vector A:\n")
A = vecA.split(" ")

#placing the input as an Array for vector A
for i in A:
    #addition in tryn to convert a str into an int
    vectorA.append(eval(i))
    
#asking for an input of vector A from the user    
vectorB = []
vecB = input("Enter vector B:\n")
B = vecB.split(" ")

#placing the input as an Array for vector A
for j in B:
    #j = eval(B)    #addition in tryn to convert a str into an int
    vectorB.append(eval(j))
 
#formulars to calculate vector addition and dot product

vector1 = ((vectorA[0])+(vectorB[0]))
vector2 =((vectorA[1])+(vectorB[1]))
vector3 = ((vectorA[2])+(vectorB[2]))
dot_product = ((vectorA[0])*(vectorB[0]))+((vectorA[1])*(vectorB[1]))+((vectorA[2])*(vectorB[2]))

#Norm of a single vector
NormA = math.sqrt((vectorA[0]**2)+(vectorA[1]**2)+(vectorA[2]**2))
NormB = math.sqrt((vectorB[0]**2)+(vectorB[1]**2)+(vectorB[2]**2))

#print it put the output
print("A+B"," ","="," ","[",vector1,","," ",vector2,","," ",vector3,"]",sep="")
print("A.B","=",dot_product)
print("|A|","=","{0:0.2f}".format(NormA))
print("|B|","=","{0:0.2f}".format(NormB))
    
    
