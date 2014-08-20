"""Assignment 6 question 2: Vector Calculations in 3 dimensions
Ailsa Mackay MCKAIL001
2014-04-22"""

import math

A = input("Enter vector A:\n")
list_A = A.split()
B = input("Enter vector B:\n")
list_B = B.split()

def add():
    component1 = int(list_A[0]) + int(list_B[0])
    component2 = int(list_A[1]) + int(list_B[1])
    component3 = int(list_A[2]) + int(list_B[2])
    add_list = [component1, component2, component3]
    print("A+B = ", add_list,sep="")

add()

def dot_product():
    component1 = int(list_A[0]) * int(list_B[0])
    component2 = int(list_A[1]) * int(list_B[1])
    component3 = int(list_A[2]) * int(list_B[2])
    product_sum = component1 + component2 + component3
    print("A.B = ", product_sum,sep="")
    
dot_product()

def normaliseA():
    square1 = int(list_A[0])**2
    square2 = int(list_A[1])**2
    square3 = int(list_A[2])**2
    normalA = math.sqrt(square1+square2+square3)
    print("|A| = ", "%.2f" % normalA, sep="")

normaliseA()

def normaliseB():
    square1 = int(list_B[0])**2 
    square2 = int(list_B[1])**2
    square3 = int(list_B[2])**2
    normalB = math.sqrt(square1+square2+square3)
    print("|B| = ", "%.2f" % normalB, sep="")

normaliseB()
    
        
      
    

