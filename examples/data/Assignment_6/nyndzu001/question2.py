"""Dzunisani Nyoni
2014 April 23
A program used for working with vectors"""

import math

#Initialize lists
A = []
B = []

vectorA= input("Enter vector A:\n")     #prompts user to enter values
vectorB= input("Enter vector B:\n")


A = vectorA.split(' ')

B = vectorB.split(' ')

#Convert values to integers

a1 = eval(A[0])
a2 = eval(A[1])
a3 = eval(A[2])

b1 = eval(B[0])
b2 = eval(B[1])
b3  =eval(B[2])


#Finding the value of vector Addition
print('A+B = ['+str(a1+b1) +', '+str(a2+b2)+', '+str(a3+b3)+']')

sum1 = a1*b1 + a2*b2 + a3*b3

print("A.B =",sum1)


def dotproduct(x1,x2,x3):
     """To find the dot product"""
    
     ans= round(math.sqrt(x1**2 + x2**2 + x3**2),2)
     return ans

if a1 ==0 and a2 ==0 and a3==0 and b1==0 and b2==0 and b3==0:
     print("|A| = 0.00")
     print("|B| = 0.00")          
    
else:
    
     print('|A| =',dotproduct(a1,a2,a3), end="\n")
     print('|B| =',dotproduct(b1,b2,b3), end="\n")

    