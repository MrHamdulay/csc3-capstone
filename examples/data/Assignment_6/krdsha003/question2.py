"""Assignment 6 Question2
Vector Calculations 
Shaheen Karodia
KRDSHA003
2014-04-20"""

import math
#get input from user and make input into a list
A=(input("Enter vector A:\n")).split()
B=(input("Enter vector B:\n")).split()


#initialise variables 
Anorm=0
Bnorm=0
dotproduct=0
addition=[]

for i in range(len(A)):    
              x= eval(A[i])
              y=eval(B[i])
              
              addition.append(x+y)   #add element to addition list
              
              dotproduct+=(x*y)      #update the value of the dotproduct
              
              
              Anorm+=x**2
              Bnorm+=y**2        
              
Anorm= "{:.2f}".format(math.sqrt(Anorm))  #format norm to display 2 digits after the decicmal place
Bnorm= "{:.2f}".format(math.sqrt(Bnorm))
             
print("A+B =", addition)
print("A.B =", dotproduct)
print("|A| =", Anorm)
print("|B| =", Bnorm)

