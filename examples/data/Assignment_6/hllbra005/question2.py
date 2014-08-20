# vector subtraction, multiplication and addition
# Brandon Hall (HLLBRA005)
# 25/04/2014

import math

A = []
B = []

def addition(A,B):
    
    R = [int(A[0]) + int(B[0]) , int(A[1]) + int(B[1]) , int(A[2]) + int(B[2])]  #Adding seperate parts of 'A' and 'B'
    print("A+B =", R) 

def dot(A,B):
    
    R = ( (int(A[0]) * int(B[0])) + (int(A[1]) * int(B[1])) + (int(A[2]) * int(B[2])) ) #Adding the products of each part of 'A' and 'B'
    print("A.B =", R)    
    
def modulus(A,B): 
    
    A_new =  math.sqrt(int(A[0])**2 + int(A[1])**2 + int(A[2])**2) #getting the absolute value of 'A'
    print("|A| =", "{0:.2f}".format(A_new))     
    
    B_new =  math.sqrt(int(B[0])**2 + int(B[1])**2 + int(B[2])**2) #Absolute value of 'B'
    print("|B| =", "{0:.2f}".format(B_new))

def main():
    
    print("Enter vector A:")

    temp = input()
    A = temp.split(" ")


    print("Enter vector B:")

    temp = input()
    B = temp.split(" ")

    addition(A,B)
    dot(A,B)
    modulus(A,B)
    
    
main()    