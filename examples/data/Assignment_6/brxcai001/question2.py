#A program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
#BRXCAI001
#25 April 2014

#Enter in values for vector and split values to make a list.
A = input("Enter vector A:\n")
listA = A.split(' ')

B = input("Enter vector B:\n")
listB = B.split(' ')

#Create equations for addition, dot product and normalization.
import math
addition = [eval(listA[0]) + eval(listB[0]), eval(listA[1]) + eval(listB[1]), eval(listA[2]) + eval(listB[2])]
dotproduct = (eval(listA[0]) * eval(listB[0])) + (eval(listA[1]) * eval(listB[1])) + (eval(listA[2]) * eval(listB[2]))
normA = math.sqrt(eval(listA[0])**2 + eval(listA[1])**2 + eval(listA[2])**2)
normAround = "{:.2f}".format(normA)
normB = math.sqrt(eval(listB[0])**2 + eval(listB[1])**2 + eval(listB[2])**2)
normBround = "{:.2f}".format(normB)

#Print out equations.
print ("A+B =", addition)
print ("A.B =", dotproduct)
print ("|A| =", normAround)
print ("|B| =", normBround)

