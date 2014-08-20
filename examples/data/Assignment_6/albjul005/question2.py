"""Program for vectors
Julian Albert
ALBJUL005
2014-04-20"""

#inputs
vector_A = input("Enter vector A:\n")
vector_B = input("Enter vector B:\n")
list_A = vector_A.split(" ")
list_B = vector_B.split(" ")

import math

#create an addition function to add values from lists A and B
def addition(vector_A,vector_B):
    list_add = []
    for i in range(3): #3 piece vectors
        add = eval(vector_A[i]) + eval(vector_B[i])
        list_add.append(add)
    print("A+B =",list_add)

#Mulitiplies the values in lists A and B. Thus returning the sum of all the products.
def product(vector_A,vector_B):
    added = 0
    for i in range(3): #3 piece vectors
        product = eval(vector_A[i]) * eval(vector_B[i]) #multiplier
        added += product
    print("A.B =",added) #prints answer

#absolute value calculation:
#absolute A
def modulus(vector_A):
    if vector_A == list_A:
        added_sqrs = 0
        for i in range(3):
            sqr = eval(vector_A[i])**2 #vector A squared
            added_sqrs += sqr
        sqrt_added_sqrs = math.sqrt(added_sqrs) #root function from math
        list_A.append("different")
        #sqrt_added_sqrs = round(sqrt_added_sqrs,2)
        print("|A| = {0:0.2f}".format(sqrt_added_sqrs))        
#absolute B
    elif vector_A == list_B:
        added_sqrs = 0
        for i in range(3):
            sqr = eval(vector_A[i])**2
            added_sqrs += sqr
        sqrt_added_sqrs = math.sqrt(added_sqrs)
        #sqrt_added_sqrs = round(sqrt_added_sqrs,2)
        print("|B| = {0:0.2f}".format(sqrt_added_sqrs))
    
addition(list_A,list_B)
product(list_A,list_B)
modulus(list_A)
modulus(list_B)
        
        