""" program to do basic vactor caluculations
Author: Rofhiwa Liphauphau
Date: 23 April 2014"""

import math

Vector_A=input("Enter vector A:\n")# getting input from user
VectorA=Vector_A.split(" ") #Splitting the string into a list
Vector_B=input("Enter vector B:\n")
VectorB=Vector_B.split(" ")

#addition function
Addition=[]
Addition.append(int(VectorA[0])+int(VectorB[0])) #adding each addition to the addition list
Addition.append(int(VectorA[1])+int(VectorB[1]))
Addition.append(int(VectorA[2])+int(VectorB[2]))
print("A+B =",Addition)

#Dot production
a=(int(VectorA[0])*int(VectorB[0]))
b=(int(VectorA[1])*int(VectorB[1]))
c=(int(VectorA[2])*int(VectorB[2]))
Final_product=a+b+c
print("A.B =",Final_product)

#Normalisation of A
a=int(VectorA[0])**2
b=int(VectorA[1])**2
c=int(VectorA[2])**2
sum=a+b+c
answer=math.sqrt(sum)
"{0:.2f}".format(answer)
print("|A| =","{0:.2f}".format(answer))  #formatting answer to 2 decimal places


#Normalisation of B
a=float(VectorB[0])**2
b=float(VectorB[1])**2
c=float(VectorB[2])**2
sum=a+b+c
answer=math.sqrt(sum)
print("|B| =","{0:0.2f}".format(answer))#formatting answer to 2 decimal places


