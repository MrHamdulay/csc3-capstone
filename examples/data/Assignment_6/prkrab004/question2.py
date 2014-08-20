#Assignment 6
#Question 2
#Rabia Parker
#Due Date:25/04/14

# program to do basic vector calculations

import math

def basic_vector():
    
    A=input("Enter vector A:\n")
    vectorA=A.split()  #create list for vectorA
    
    B=input("Enter vector B:\n")
    vectorB=B.split() #create list for vectorB
    
    #working out the sum and creating a list
    sumlist=[]
    if len(vectorA) == len(vectorB):
        for i in range(len(vectorA)):
            a=eval(vectorA[i]) + eval(vectorB[i]) #the sum of two numbers
            sumlist.append(a) #add to the end of the list
    print("A+B = ",sumlist,sep="")
    
    #working out the product and creating a list
    r=0
    if len(vectorA) == len(vectorB):
        for j in range(len(vectorA)):
            product = eval(vectorA[j]) * eval(vectorB[j]) #multiply vectors
            r+=product
    print("A.B =", r)
    
    #normalise the vector A
    normalA = 0
    for r in range(len(vectorA)):
        normal = eval(vectorA[r])**2
        normalA += normal
    x = math.sqrt(normalA) #square to make it positive
    if vectorA==["0","0","0"]:
        print("|A| = 0.00")
    else:
        print("|A| =", round(x,2))
    
    #normlise vector B
    normalB = 0
    for b in range(len(vectorB)):
        normal = eval(vectorB[b])**2
        normalB += normal
    x = math.sqrt(normalB) #square to make it positive
    if vectorB==["0","0","0"]:
        print("|B| = 0.00")
    else:
        print("|B| =", round(x,2))
    
        
        
basic_vector()
