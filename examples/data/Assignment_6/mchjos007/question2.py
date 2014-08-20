#code to enter the components of two 3-dimensional vectors and return their addition, dot product and normalization. Joshua Michelson 22/04/2014#
import math
vectorA = input("Enter vector A:\n").split(" ")
vectorB = input("Enter vector B:\n").split(" ")
print("A+B = ["+str(eval(vectorA[0])+eval(vectorB[0]))+", "+str(eval(vectorA[1])+eval(vectorB[1]))+", "+str(eval(vectorA[2])+eval(vectorB[2]))+"]")
print("A.B = "+str((eval(vectorA[0])*eval(vectorB[0]))+(eval(vectorA[1])*eval(vectorB[1]))+(eval(vectorA[2])*eval(vectorB[2]))))
print("|A| = " +"{0:.2f}".format(round(math.sqrt((eval(vectorA[0])**2)+(eval(vectorA[1])**2)+(eval(vectorA[2])**2)),2)))
print("|B| = " +"{0:.2f}".format(round(math.sqrt((eval(vectorB[0])**2)+(eval(vectorB[1])**2)+(eval(vectorB[2])**2)),2)))