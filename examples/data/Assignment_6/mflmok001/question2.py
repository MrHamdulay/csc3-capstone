
"""Mokoena Mafologele
Vector calculations program
22/04/2014"""
import math

#Get vector A via prompt
a=input("Enter vector A:\n").split(" ")
a=[eval(a[0]),eval(a[1]),eval(a[2])]

#Get vector B via prompt
b=input("Enter vector B:\n").split(" ")
b=[eval(b[0]),eval(b[1]),eval(b[2])]

#initialise calculations
sumv=[a[0]+b[0],a[1]+b[1],a[2]+b[2]] #addition of vectors
dotprod=a[0]*b[0]+a[1]*b[1]+a[2]*b[2] # product of the vectors
magnitudeA=math.sqrt(math.pow(a[0],2)+math.pow(a[1],2)+math.pow(a[2],2)) #size of vector A
magnitudeB=math.sqrt(math.pow(b[0],2)+math.pow(b[1],2)+math.pow(b[2],2)) #size of vector B

#output results
print("A+B =",sumv,"\nA.B =",dotprod,"\n|A| =",("%0.2f")%(magnitudeA),"\n|B| =",("%0.2f")%(magnitudeB))



