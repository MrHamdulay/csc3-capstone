"""Program to perform basic vector calculations
Pankaj Munbodh
20 April 2014"""

# Get input for vectors A and B from user and create lists for them
A=input("Enter vector A:\n").split()
B=input("Enter vector B:\n").split()

#Addition of A and B
def Sum():
    Sum=[]
    for a,b in zip(A,B): #zip used to loop over two or more sequences at a time
        sum1=eval(a)+eval(b)
        Sum.append(sum1)
    return Sum

print("A+B =",Sum())

#Dot product of A and B
def Dot():
    dot=0
    for a,b in zip(A,B):
        dot1=eval(a)*eval(b)
        dot+=dot1
    return dot

print("A.B =",Dot())

#Normalisation of vectors
import math
def Normvec(A):
    modulus=0     #initialising accumulator variable
    for a in A:
        modulus+= eval(a)**2
    modulus=math.sqrt(modulus)
    modulus="{0:0.2f}".format(modulus) #format can be used to specify number of dp or sf. Here, number of dp is specified to be 2.
    return modulus
print("|A| =",Normvec(A))
print("|B| =",Normvec(B))
