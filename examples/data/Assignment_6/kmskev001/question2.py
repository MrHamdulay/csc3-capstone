"""program to calcualte basic vectors 
   kevin kumasamba
   22 april 2014"""

import math

# making a list of vectors a and b
a=input("Enter vector A:\n")
A=a.split(" ") # the numbers are still strings at this point
b=input("Enter vector B:\n")
B=b.split(" ")

add_list=[] # you need this for the values of the added vectors
prod_list=[]
square_list=[]
square_listB=[]
sumprod=0
sum_square=0
sum_squareB=0

#adding the vectors
for i in range(3):
    add_vectors=eval(A[i])+eval(B[i])
    add_list.append(add_vectors)
print("A+B =", add_list)

#the sum of the products
for i in range(3):
    prod_vectors=eval(A[i])*eval(B[i])
    prod_list.append(prod_vectors)
    # print(prod_list)
for i in prod_list:
    sumprod+=i
print("A.B =", sumprod)

#sqrt of the sum of the square vectors
for i in A:
    i=eval(i)
    new_i=i**2
    square_list.append(new_i)
for i in square_list:
    sum_square+=i
if sum_square==0:
    print("|A| = 0.00")    
    #print(i)
#print(sum_square)
else:
    print("|A| =", round(math.sqrt(sum_square), 2))

for i in B:
    i=eval(i)
    new_i=i**2
    square_listB.append(new_i)
for i in square_listB:
    sum_squareB+=i
if sum_squareB==0:
    print("|B| = 0.00")
else:
    print("|B| =", round(math.sqrt(sum_squareB), 2))




