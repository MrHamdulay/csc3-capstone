"""Program to do basic vector calculations in 3 dimensions
Sithasibanzi Kondleka
24 April 2014"""

import math
vector1 = input("Enter vector A:\n")
x = vector1.split(" ")
#print(x)

vector2 = input("Enter vector B:\n")
y = vector2.split(" ")
#print(y)

print("A+B = [",(eval(x[0])+eval(y[0])),", ",(eval(x[1])+eval(y[1])),", ",(eval(x[2])+eval(y[2])),"]",sep="") #add numbers in positions 1, 2 & 3
print("A.B = ",(eval(x[0])*eval(y[0]))+(eval(x[1])*eval(y[1]))+(eval(x[2])*eval(y[2])),sep="") #multiply numbers in positions 1, 2 & 3
print("|A| = ",round(math.sqrt((eval(x[0])*eval(x[0]))+(eval(x[1])*eval(x[1]))+(eval(x[2])*eval(x[2]))),2),sep="") #get the square root of A
print("|B| = ",round(math.sqrt((eval(y[0])*eval(y[0]))+(eval(y[1])*eval(y[1]))+(eval(y[2])*eval(y[2]))),2),sep="") #get the square root of B