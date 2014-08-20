"""program for vector calculations
casey o'donnell
21 april 2014"""

import math

A=input("Enter vector A:\n").split(" ")
B=input("Enter vector B:\n").split(" ")

def add(A,B):
    C=[]
    for i in range(len(A)):
        C.append(int(A[i])+int(B[i]))
    print("A+B =",C)
    
def mult(A,B):
    C=0
    for i in range(len(A)):
        C+=int(A[i])*int(B[i])
    print("A.B =", C)
    
def normA(A):
    C=0
    for i in range(len(A)):
        C+=int(A[i])**2
    C=math.sqrt(C)
    C=round(C,2)
    print("|A| =","{0:.2f}".format(C,2))
    
def normB(B):
    C=0
    for i in range(len(B)):
        C+=int(B[i])**2
    C=math.sqrt(C)
    C=round(C,2)
    print("|B| =","{0:.2f}".format(C,2))
        
        
add(A,B)
mult(A,B)  
normA(A)
normB(B)