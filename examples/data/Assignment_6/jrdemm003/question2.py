"""assignment 6 question 2. program to do vector calculations
emma jordi
20 april 2014"""

import math

#set empty lists
listA= []
listB= []
#get vector values as lists
listA= input("Enter vector A:\n")
listA=listA.split()

listB= input("Enter vector B:\n")
listB=listB.split()

#def function for addition
SUM1 =eval(listA[0])+eval(listB[0])
SUM2= eval(listA[1]) + eval(listB[1])
SUM3= eval(listA[2]) + eval(listB[2])
 

#def function for dot production
PROD1 =eval(listA[0]) * eval(listB[0])
PROD2= eval(listA[1]) * eval(listB[1])
PROD3= eval(listA[2]) * eval(listB[2])

#def function for normalization

NORM_A= math.sqrt((eval(listA[0]) ** 2) + (eval(listA[1]) ** 2) + (eval(listA[2]) ** 2))    
NORM_B= math.sqrt((eval(listB[0]) ** 2) + (eval(listB[1]) ** 2) + (eval(listB[2]) ** 2))

#must round off to 2 dec points. 0.00
f="{0:0<4}"
    
print("A+B = [",str(SUM1),",", " "+str(SUM2),","," "+str(SUM3)+"","]",sep="")
print("A.B =", PROD1+PROD2+PROD3)
print("|A| =", f.format(round(NORM_A,2)))
print("|B| =", f.format(round(NORM_B,2)))

