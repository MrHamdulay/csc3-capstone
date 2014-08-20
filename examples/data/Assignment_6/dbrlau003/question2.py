#Lauren de Bruyn
#Program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
#22 April 2014

import math

#user inputs vector A and B and then split vectors into lists
A=input("Enter vector A: \n")
B=input("Enter vector B: \n")
list_A = A.split(" ")
list_B = B.split(" ")
    
#addition of two lists
newlist=[]
for i in range(3):    
    x=eval(list_A[i])+eval(list_B[i])
    newlist.append(x)
print("A+B =",newlist)

#dot product of A and B
sumproducts=0
for i in range(3):
    z=eval(list_A[i])*eval(list_B[i])
    sumproducts=sumproducts+z
print("A.B =",sumproducts)

#Norm of a single vector: the square root of the sum of the squares of the elements
sumAsquares=0
for i in range(3):
    y=eval(list_A[i])**2
    sumAsquares=sumAsquares+y
x=math.sqrt(sumAsquares)
a="{:.2f}".format(x)
print("|A|","=",a)

sumBsquares=0
for i in range(3):
    n=eval(list_B[i])**2
    sumBsquares=sumBsquares+n
x=math.sqrt(sumBsquares)
a="{:.2f}".format(x)
print("|B|","=",a)

    