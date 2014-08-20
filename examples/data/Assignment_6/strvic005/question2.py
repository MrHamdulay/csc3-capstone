"""program to do basic vector calc
vicky stark
23 april 2014"""

import math

#create an array for vector A
list_1=[]
x=input("Enter vector A:\n")
x.split()
for i in x:
    list_1.append(i)
    
#create an array for vector B
list_2=[]
y=input("Enter vector B:\n")
y.split()
for j in y:
    list_2.append(j)
    
#addition
a=eval(list_1[0])+eval(list_2[0])
b=eval(list_1[2])+eval(list_2[2]) #indexing position 2 due to spaces in list
c=eval(list_1[4])+eval(list_2[4]) #indexing position 4 due to spaces in list
list_3=[a,b,c]
print("A+B =", list_3)

#dot product
d=eval(list_1[0])*eval(list_2[0])
e=eval(list_1[2])*eval(list_2[2]) #indexing position 2 due to spaces in list
f=eval(list_1[4])*eval(list_2[4]) #indexing position 4 due to spaces in list
product=d+e+f
print("A.B =", product)

#normalization for A
square=(eval(list_1[0])**2)+(eval(list_1[2])**2)+(eval(list_1[4])**2)
sqrt=math.sqrt(square)
print("|A| =", "{:.2f}".format(round(sqrt,2))) #use format to fill spaces with zero

#normalization for B
square_2=(eval(list_2[0])**2)+(eval(list_2[2])**2)+(eval(list_2[4])**2)
sqrt_2=math.sqrt(square_2)
print("|B| =", "{:.2f}".format(round(sqrt_2, 2)))

