"""Sphiwe Muthembi
   Mthsph007
   Assignment 6 - Question 2
   Vector calculator"""

#create two lists for vector values
#split text
#eval values and do calculations
# create functions to separate operations
import math
#INPUTS
vecA= input('Enter vector A:\n')
vecB= input('Enter vector B:\n')

#List / Arrays
A = []
B = []

A = vecA.split(' ')
B = vecB.split(' ')

#making values into integer format

a1,a2,a3 = eval(A[0]), eval(A[1]), eval(A[2])
b1,b2,b3 = eval(B[0]), eval(B[1]), eval(B[2])

# Outputing the first two irriatations.
print('A+B = ['+str(a1+b1) +', '+str(a2+b2)+', '+str(a3+b3)+']')

multi_sum = a1*b1 + a2*b2 + a3*b3

print("A.B =",multi_sum)

# have a single function to calculate sqrt of both vectors

def square(x1,x2,x3):
    
    root = round(math.sqrt(x1**2 + x2**2 + x3**2),2)
    return root

if a1 ==0 and a2 ==0 and a3==0 and b1==0 and b2==0 and b3==0:
    print('|A| = 0.00')
    print("|B| = 0.00")             # print this if values inputted are == 0.
    
else:
    

    print('|A| =',square(a1,a2,a3))
    print('|B| =',square(b1,b2,b3))

    