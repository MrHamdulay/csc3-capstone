#Ariel Rubin
#RBNARI001
#23 April 2014
# program to show vector subtraction, multiplication and addition

import math

#creating 2 different arrays
A = []
B = []

def addition(A,B):
    
    R = [int(A[0]) + int(B[0]) , int(A[1]) + int(B[1]) , int(A[2]) + int(B[2])]  #Adding seperate parts of 'A' and 'B'
    print("A+B =", R) 

def product(A,B):
    
    R = ( (int(A[0]) * int(B[0])) + (int(A[1]) * int(B[1])) + (int(A[2]) * int(B[2])) ) #Adding the products of each part of 'A' and 'B'
    print("A.B =", R)    
    
def modular(A,B): 
    
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

#calling all 3 functions 
    addition(A,B)
    product(A,B)
    modular(A,B)
    
    
main()    