""" Vector Calculations 
Tameryn Pillay
23 April 2014 """

import math

def main():
    
    # ask the user for vectors
    a = (input("Enter vector A:\n"))
    A = a.split()
    
    b = (input("Enter vector B:\n"))
    B = b.split()
    
    # addition
    x = int(A[0])+int(B[0])
    y = int(A[1])+int(B[1])
    z = int(A[2])+int(B[2])
    
    # dot product
    a = int(A[0])*int(B[0])
    b = int(A[1])*int(B[1])
    c = int(A[2])*int(B[2])
    
    # norm of a single vector
    d = int(A[0])**2
    e = int(A[1])**2
    f = int(A[2])**2
    
    h = int(B[0])**2
    j = int(B[1])**2
    k = int(B[2])**2
    
    # output
    print("A+B = ","[",x,", ",y,", ",z ,"]",sep='')
    print("A.B = ",a+b+c,sep='')
    print("|A| = ",round(math.sqrt(d+e+f),2),sep='')
    print("|B| = ",round(math.sqrt(h+j+k),2),sep='')
    
main()