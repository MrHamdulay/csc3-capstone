"""Program to output basic vector calculations (Question 2)
24 April 2014
Jaren Hendricks"""

import math

# Empty lists
add = []
Multi = []
sqA = []
sqB =[]

# Gets values and adds the values to the array
arrA = input("Enter vector A:\n").split(' ')
arrB = input("Enter vector B:\n").split(' ')

# function to add and multiply vectors
def Add_Multiply(A,B):
    for i in range(3):
        A, B = eval(arrA[i]), eval(arrB[i])
        add.append(A+B)
        Multi.append(A*B)
    ans= Multi[0] + Multi[1] + Multi[2] 
    print("A+B =", add)
    print("A.B =", ans)

# function to output the square root of the sum of the squares of the vector values
def SquareRoot (A,B):
    for i in range(3):
        A, B = eval(arrA[i])**2, eval(arrB[i])**2
        sqA.append(A)
        sqB.append(B)
    ansA= math.sqrt(sqA[0] + sqA[1] + sqA[2]) 
    ansB= math.sqrt(sqB[0] + sqB[1] + sqB[2]) 
    print("|A| =", '{0:0.2f}'.format(ansA))
    print("|B| =",'{0:0.2f}'.format(ansB))
        

# Calling functions
Add_Multiply(arrA,arrB)
SquareRoot (arrA,arrB) 