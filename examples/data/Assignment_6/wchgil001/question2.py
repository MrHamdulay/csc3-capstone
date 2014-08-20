#gillian wachira, 24/04/2014, arrays.
A=input("Enter vector A:\n")
B=input("Enter vector B:\n")
vecA=A.split()
vecB=B.split()
#addition
addition=[eval(vecA[0])+eval(vecB[0]), eval(vecA[1])+eval(vecB[1]), eval(vecA[2])+eval(vecB[2])]
#product
product=eval(vecA[0])*eval(vecB[0])+eval(vecA[1])*eval(vecB[1])+eval(vecA[2])*eval(vecB[2])
import math
#dot.product
dotproductA=math.sqrt((eval(vecA[0])**2+eval(vecA[1])**2+eval(vecA[2])**2))
dotproductB=math.sqrt((eval(vecB[0])**2+eval(vecB[1])**2+eval(vecB[2])**2))
print("A+B =",addition)
print("A.B =",product)
print("|A| =",'{0:.2f}'.format(dotproductA))
print("|B| =",'{0:.2f}'.format(dotproductB))

