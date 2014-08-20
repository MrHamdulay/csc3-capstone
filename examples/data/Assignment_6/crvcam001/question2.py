# question2.py
# program to do basic vector calculations in three dimensions
# camilla craven
# 24 april 2014

import math # imports maths library

# creating function to add vectors
def addition(A,B):
   
    vector = []
  
    # A+B is calculated and added to the list for each value
    for i in range(3): 
        vector.append((eval(A[i]) + eval(B[i]))) 
  
    print("A+B = ", vector, sep = "") 


# creating function to multiply vectors
def dot_product(A,B):
   
    product = 0
   
    # multiplying A each value in A by each value in B
    for i in range(3):
        product += eval(A[i]) * eval(B[i]) 
        
    print("A.B = ", product, sep = "") 


# creating function to find norm of vector A
def norm_A(A):
    
    a = 0
   
    # sum of squares of each value in vector A
    for i in range(3):
        a += eval(A[i]) * eval(A[i])  
    
    # squarerooting calculated value above and rounding to 2 dec pl  
    norm = round(math.sqrt(a), 2)
    
    if norm == 0:
        print("|A| = 0.00") # 2 dec pl if 0
    else:
        print("|A| = ",norm, sep = "") 


# creating function to find norm of vector A
def norm_B(B):
    
    # same process as norm of A, except using values of vector B
    b = 0    
    for i in range(3):
        b += eval(B[i]) * eval(B[i])   
    norm = round(math.sqrt(b), 2)
    
    if norm == 0:
        print("|B| = 0.00") 
    else:
        print("|B| = ", norm, sep = "")
   
    
def main():
    
    A = []
    B = []
    
    # prompts user for vector values
    List_A = input("Enter vector A:\n")
    List_B = input("Enter vector B:\n")
    
    # splits strings by spaces and adds to list
    A = List_A.split()
    B = List_B.split()
    
    # use functions created above
    addition(A,B)
    dot_product(A,B) 
    norm_A(A)
    norm_B(B)
    
main()