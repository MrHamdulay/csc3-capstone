# Lehlogonolo Masetla
# 22 April 2014

import math

vector_a = (input("Enter vector A:\n"))

vector_a.split(" ")

vector_b = input("Enter vector B:\n")

vector_b.split(" ")

x = vector_a.split()
y = vector_b.split()

#print(x,y)

addition1 = eval(x[0]) + eval(y[0])
addition2 = eval(x[1]) + eval(y[1])
addition3 = eval(x[2]) + eval(y[2])

#Vactor dot product
dproduct1 = eval(x[0]) * eval(y[0]) + eval(x[1]) * eval(y[1]) + eval(x[2]) * eval(y[2])

# Vector normalization
normalA = math.sqrt(eval(x[0])*eval(x[0])+eval(x[1])*eval(x[1])+eval(x[2])*eval(x[2]))
normalB = math.sqrt(eval(y[0])*eval(y[0])+eval(y[1])*eval(y[1])+eval(y[2])*eval(y[2]))

print("A+B"," ","="," ","[",addition1,","," ",addition2,","," ",addition3,"]",sep="")
print("A.B"," ","="," ",dproduct1,sep="")
print("|A|","=","{0:.{1}f}".format(normalA,2))
print("|B|","=","{0:.{1}f}".format(normalB,2))