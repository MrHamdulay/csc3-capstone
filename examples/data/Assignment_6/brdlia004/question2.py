"""3D Vector calculator"""
#Liam Brodie
#4.20 2014
#BRDLIA004

import math

a = input("Enter vector A:\n")
vecA = a.split(" ")

b = input("Enter vector B:\n")
vecB = b.split(" ")

AB = [eval(vecA[0])+eval(vecB[0]), eval(vecA[1])+eval(vecB[1]), eval(vecA[2])+eval(vecB[2])]
print("A+B =", AB)

AxB = eval(vecA[0])*eval(vecB[0]) + eval(vecA[1])*eval(vecB[1]) + eval(vecA[2])*eval(vecB[2])
print("A.B =", AxB)

sqA = math.sqrt(eval(vecA[0])**2 + eval(vecA[1])**2 + eval(vecA[2])**2)
print("|A| =", "{0:.{1}f}".format(sqA, 2))

sqB = math.sqrt(eval(vecB[0])**2 + eval(vecB[1])**2 + eval(vecB[2])**2)
print("|B| =", "{0:.{1}f}".format(sqB, 2))