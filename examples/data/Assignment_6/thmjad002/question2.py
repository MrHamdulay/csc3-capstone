"""Asignment 6, Question 2
JT
23-04-2014"""

A = input("Enter vector A:\n")
B = input("Enter vector B:\n")
listA = A.split(" ")
listB = B.split(" ")

import math

#create an addition function to add corresponding values from lists A and B
def addition(A,B):
    list_add = []
    for i in range(3):
        add = eval(A[i]) + eval(B[i])
        list_add.append(add)
    print("A+B =",list_add)

#Mulitiplies the corresponding values in lists A and B and the adds them to a variable call added_prods. Thus returning the sum of all the products.
def product(A,B):
    added_prods = 0
    for i in range(3):
        prod = eval(A[i]) * eval(B[i])
        added_prods += prod
    print("A.B =",added_prods)
        
def norm(A):
    if A == listA:
        added_sqrs = 0
        for i in range(3):
            sqr = eval(A[i])**2
            added_sqrs += sqr
        sqrt_added_sqrs = math.sqrt(added_sqrs)
        listA.append("different")
        #sqrt_added_sqrs = round(sqrt_added_sqrs,2)
        print("|A| = {0:0.2f}".format(sqrt_added_sqrs))        
        
    elif A == listB:
        added_sqrs = 0
        for i in range(3):
            sqr = eval(A[i])**2
            added_sqrs += sqr
        sqrt_added_sqrs = math.sqrt(added_sqrs)
        #sqrt_added_sqrs = round(sqrt_added_sqrs,2)
        print("|B| = {0:0.2f}".format(sqrt_added_sqrs))
    
addition(listA,listB)
product(listA,listB)
norm(listA)
norm(listB)
        
        