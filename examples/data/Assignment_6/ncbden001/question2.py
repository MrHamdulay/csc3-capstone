#Program too work with vectors
#Denzel Ncube
#22 April 2014
import math
#Getting input
A = input("Enter vector A:\n")
B = input("Enter vector B:\n")
#Splitting input into lists
vectorA = A.split(" ")     
vectorB = B.split(" ")
#Addition calculation
Addition = [int(vectorA[0])+int(vectorB[0]),int(vectorA[1])+ int(vectorB[1]),int(vectorA[2])+ int(vectorB[2])]
#Multiplication calculation
Multiplication = (int(vectorA[0])*int(vectorB[0]))+(int(vectorA[1])* int(vectorB[1])) + (int(vectorA[2])* int(vectorB[2]))
#Norm Calculations
NormA = round(math.sqrt(int(vectorA[0])**2 + int(vectorA[1])**2 + int(vectorA[2])**2),2)
NormB = round(math.sqrt(int(vectorB[0])**2 + int(vectorB[1])**2 + int(vectorB[2])**2),2)
#Displaying everything
print("A+B =",Addition)
print("A.B =",Multiplication)
if NormA == 0.0:
    print("|A| =","0.00")          
else:
    print("|A| =",NormA)    
if NormB == 0.0:
    print("|B| =","0.00")
else:
    print("|B| =",NormB)