"""Assignment 6
question 2
Mphuthi MAamorena
20 april 2014"""

A=input("Enter vector A:\n")
B=input("Enter vector B:\n")

# turning them into list
A=A.split(' ')
B=B.split(' ')

# adding them together
first=eval(A[0])+eval(B[0])
second=eval(A[1])+eval(B[1])
third=eval(A[2])+eval(B[2])
print('A+B =','['+str(first)+',',str(second)+',',str(third)+']')

# dot product
x=eval(A[0])*eval(B[0])

y=eval(A[1])*eval(B[1])

z=eval(A[2])*eval(B[2])

dotpro=z+x+y
print('A.B =',round(dotpro))

import math

#normalization

one=eval(A[0])
two=eval(A[1])
three=eval(A[2])  

Sum=one**2+two**2+three**2
nom=math.sqrt(Sum)
if nom==0:
    print('|A| =','0.00')
else:
    print('|A| =',round(nom,2))

oneB=eval(B[0])
twoB=eval(B[1])
threeB=eval(B[2])  

SumB=oneB**2+twoB**2+threeB**2
nomB=math.sqrt(SumB)
if nomB==0:
    print('|B| =','0.00')
else:
    print('|B| =',round(nomB,2))
