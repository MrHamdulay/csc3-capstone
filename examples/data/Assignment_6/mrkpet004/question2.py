""" program to do basic vector calculations in 3 dimensions: addition, dot product and normalization
peter m muriuki"""
import math

#get two different vectors and add them into two different lists
x,y,a,b=0,0,0,0
sumX=[]
v_listA=input("Enter vector A:\n")
v_listB=input("Enter vector B:\n")
vectorA=v_listA.split(" ")
vectorB=v_listB.split(" ")

#calculate the sum,dot product of the two vectors and normalised values for the vectors and store the results
for i in range(len(vectorA)):
    x = int(vectorA[i]) + int(vectorB[i])
    y += int(vectorA[i]) * int(vectorB[i])
    a += int(vectorA[i])**2
    b += int(vectorB[i])**2
    sumX.append(x) #add the sum of the vectors into am initialised list

#print out the results of the vector calculations    
print ("A+B =",sumX)
print ("A.B =",y)
print ("|A| =","{:0.2f}".format(math.sqrt(a)))
print ("|B| =","{:0.2f}".format(math.sqrt(b)))