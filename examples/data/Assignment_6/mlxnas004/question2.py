"""nasha somoina meoli
24th april 2014
program to do vector addition, dot product and normalization"""

import math

def vectors():
    A = input("Enter vector A:\n")
    A = A.split(" ")
    #print(A)
    B = input("Enter vector B:\n")
    B = B.split(" ") 
    #to add the vectors
    sumlist=[]
    for i in range(3):
        sum= eval(A[i])+eval(B[i])
        sumlist.append(sum)
    print("A+B =",sumlist)
    # to get the dot product
    sumproduct=0
    for i in range(3):
        product= eval(A[i])*eval(B[i])
        sumproduct+=product
    print("A.B =",sumproduct)
    #to get the norms
    sumnorm = 0
    for i in range(3):
        norm = eval(A[i])**2
        #print(norm)
        sumnorm+=norm
    newnormal = round((math.sqrt(sumnorm)),2)
    if newnormal == (0.0):
        normal= "0.00"
    else:
        normal=newnormal
    print("|A| =",normal)
    sumnorm2 = 0
    for i in range(3):
        norm2 = eval(B[i])**2
        #print(norm)
        sumnorm2+=norm2
    normal2 = round(math.sqrt(sumnorm2),2)
    if normal2 == 0:
        normal2= "0.00"
    print("|B| =",normal2)
    
        
vectors()