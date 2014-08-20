"""vector calculations
kennedy muranda
24/4/2014"""

#diifferent vectors
A = []
B = []

#prompt user to add values to lists
vectorA = input("Enter vector A:\n")
vectorB = input("Enter vector B:\n")

#split strings
A = vectorA.split(' ')
B = vectorB.split(' ')

import math

#addition function
def addition():
    list_Add = []
    for i in range(len(A)):
        list_Add.append (eval(A[i]) + eval(B[i]))
    print("A+B =",list_Add,end='')
    
#dot product
def product():
    list_Product = []
    for n in range(len(A)):
        list_Product.append (eval(A[n])*eval(B[n]))
    print("A.B =",list_Product[0] + list_Product[1] + list_Product[2])

#normalisation for A
def normA():
    list_normA = []
    for j in range(len(A)):
        list_normA.append (eval(A[j])*eval(A[j]))
    squareA = math.sqrt(list_normA[0] + list_normA[1] + list_normA[2])
    roundA = "%.2f"%squareA
    print("|A| =", roundA)
    
#normalisation for B
def normB():
    list_normB = []
    for k in range(len(B)):
        list_normB.append (eval(B[k])*eval(B[k]))
    squareB = math.sqrt(list_normB[0] + list_normB[1] + list_normB[2])
    roundB = "%.2f"%squareB
    print("|B| =",roundB)
    
    
addition()
print()
product()
normA()
normB()

    
    
    
    











    
    