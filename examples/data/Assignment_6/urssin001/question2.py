'''Program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
Sinead Urisohn
19 April 2014
'''
import math
#Get vector A and B
vectorA=input("Enter vector A:\n")
vectorB=input("Enter vector B:\n")
#Get vectors as arrays
A=vectorA.split()
B=vectorB.split()
#Get components of vectors using indexing
a1=int(A[0])
a2=int(A[1])
a3=int(A[2])
b1=int(B[0])
b2=int(B[1])
b3=int(B[2])
#do A+B 
AplusB="["+str(a1+b1)+", "+str(a2+b2)+", "+str(a3+b3)+"]"

#do A.B 
AdotB=(a1*b1+a2*b2+a3*b3)



#do |A| round 2 dec places using format
txt='{0:.2f}'
normA=math.sqrt(a1**2+a2**2+a3**2)

#do |B| round 2 dec places
normB=math.sqrt(b1**2+b2**2+b3**2)

#print data in readable message
print("A+B = "+AplusB+"\nA.B = "+str(AdotB)+"\n|A| = "+txt.format(normA)+"\n|B| = "+txt.format(normB))