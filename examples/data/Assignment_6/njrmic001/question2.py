#A program to do basic vector calculations in 3 dimensions
#Author: Michelle Njoroge
#24 April 2014

import math

Vector_A=input("Enter vector A:\n")
Vector_B=input("Enter vector B:\n")

Vector_A=Vector_A.split()
Vector_B=Vector_B.split()
Addition=[]

Addition.append(int(Vector_A[0])+int(Vector_B[0]))
Addition.append(int(Vector_A[1])+int(Vector_B[1]))
Addition.append(int(Vector_A[2])+int(Vector_B[2]))

number1=int(Vector_A[0])*int(Vector_B[0])
number2=int(Vector_A[1])*int(Vector_B[1])
number3=int(Vector_A[2])*int(Vector_B[2])

Product=(number1+number2+number3)

squarea1=int(Vector_A[0])**2
squarea2=int(Vector_A[1])**2
squarea3=int(Vector_A[2])**2

squareA=math.sqrt(squarea1+squarea2+squarea3)

squareb1=int(Vector_B[0])**2
squareb2=int(Vector_B[1])**2
squareb3=int(Vector_B[2])**2

squareB=math.sqrt(squareb1+squareb2+squareb3)

print("A+B","=",Addition)
print("A.B","=",Product)
print("|A|","=","{0:.2f}".format(squareA))
print("|B|","=","{0:.2f}".format(squareB))



    