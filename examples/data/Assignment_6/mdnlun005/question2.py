#-------------------------------------------------------------------------------
# Name:        question2
# Purpose:     a program to do basic vector calculations in 3 dimensions:
#               addition, dot product and normalization
#
# Author:      Lungelo Mdunge
#
# Created:     21/04/2014
# Copyright:   (c) Lungelo 2014
#-------------------------------------------------------------------------------

import math

#get input
vectorA=input("Enter vector A:\n").split(' ')
vectorB=input("Enter vector B:\n").split(' ')

#add the two vectors and print
sumVector=[]
for i in range(len(vectorA)):
    sumVector.append(eval(vectorA[i])+eval(vectorB[i]))
print("A+B =",sumVector)

#multiplies the corresponsing array values and adds their products
product=0
for i in range(len(vectorA)):
    product+=(eval(vectorA[i])*eval(vectorB[i]))
print("A.B =",product)

#normalization of vectorA
Sum=0
for i in vectorA:
    i=eval(i)**2
    Sum+=i
print("|A| =",'{0:.2f}'.format(math.sqrt(Sum)))

Sum=0
for i in vectorB:
    i=eval(i)**2
    Sum+=i
print("|B| =",'{0:.2f}'.format(math.sqrt(Sum)))