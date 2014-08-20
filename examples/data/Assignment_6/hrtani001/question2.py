#Vector calculator
#Aniq Hartle
#25/04/2014

import math

#take and split inputs into arrays
vectorA = input("Enter vector A:\n").split(" ")
vectorB = input("Enter vector B:\n").split(" ")

#print output using array contents in formula
print("A+B = [",eval(vectorA[0])+eval(vectorB[0]),", ", eval(vectorA[1])+eval(vectorB[1]), ", ",eval(vectorA[2])+eval(vectorB[2]), sep="", end="]\n")
print("A.B = ",eval(vectorA[0])*eval(vectorB[0])+eval(vectorA[1])*eval(vectorB[1])+eval(vectorA[2])*eval(vectorB[2]),sep="")
print("|A| = {:.2f}".format(math.sqrt((eval(vectorA[0])**2)+(eval(vectorA[1])**2)+(eval(vectorA[2])**2)),2))
print("|B| = {:.2f}".format(math.sqrt((eval(vectorB[0])**2)+(eval(vectorB[1])**2)+(eval(vectorB[2])**2)),2))