# a program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
# Budeli Rendani
# BDLREN001
# 20/04/2014

import math # importing the math function
def main():
    A=[] # An empty list for vector A
    B=[] # An empty list for vector B
    a=input("Enter vector A:\n").split() # Obtaining input from the user seperated by empty spaces
    for i in a:
        i=eval(i) # Converting the input to an integer
        A.append(i) #Adding the inputs to the empty list
    
    b=input("Enter vector B:\n").split() # Obtaining input from the user seperated by empty spaces
    for j in (b):
        j=eval(j) # Converting the input to an integer
        B.append(j) # Adding the inputs to the empty list
        
    AB=[a+b for a,b in zip(A,B)] # Adding the corresponding values of list A and B with each other
    print("A+B =",AB)
    n=[i*j for i,j in zip(A,B)] # Finding the product of the corresponding values in the two lists
    z=sum([i*j for i,j in zip(A,B)]) # Finding the sum of the of the product of the corresponding values in the two lists
    print("A.B =",z)
    k=[] # Creating an empty list for the square root of the values in list A
    for u in A:
        f=u**2 # finding the square root of the values in list A
        k.append(f) # Adding the values to list K
    g=sum(k) # Finding the sum of the values in list K
    h=g**(1/2) # Finding the square root of the values in list K
    print("|A| =","%.2f"%h) # Printing of the rounded answer to two decimal places
    p=[] # Creating an empty list for the square root of the values in list B
    for t in B:
        c=t**2 # finding the square root of the values in list A
        p.append(c) # Adding the values to list p
    v=sum(p) # Finding the sum of the values in list p
    o=v**(1/2) # Finding the square root of the values in list p
    print("|B| =","%.2f"%o) # Printing of the rounded answer to two decimal places
       
main()