#Program to calculate addition of vectors, dot product and the norm
#Shane Horsley
#22 April 2014
import math # to use sqrt function
a = (input("Enter vector A:\n")) # get values for first list
b = (input("Enter vector B:\n")) # get values for 2nd list
LA=[]
LB=[]
for i in a.split(" "): # add values to list LA
    LA.append(int(i))
for i in b.split(" "): # add values to list LB
    LB.append(int(i))

list_add = [] # new list for sum of corresponding vectors
for i in range(len(LA)): # summimg of correspong vectors in 2 lists
    x = LA[i]+LB[i]
    list_add.append(x)
print("A+B =", list_add)
x=0
for i in range(len(LA)): # calculate dot product
    x += LA[i]*LB[i]
print("A.B =",x)

y=0
for i in range(len(LA)): # norm of LA
    y += LA[i]**2 # adding square of each item in list
if math.sqrt(y) == 0: # because round doesnt work for 0
    print("|A| = 0.00")
else:
    print("|A| =",round(math.sqrt(y),2))

z=0
for i in range(len(LB)): # same as above but for LB
    z += LB[i]**2
if math.sqrt(z) == 0:
    print("|B| = 0.00")
else:
    print("|B| =", round(math.sqrt(z),2))             

