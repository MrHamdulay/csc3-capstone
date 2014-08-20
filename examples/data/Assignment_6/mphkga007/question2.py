""" program that calculates vectors
kenneth mphele
21/04/2014"""
import math

def vectors():
    A=input("Enter vector A:\n")
    B=input("Enter vector B:\n")
    a=A.split(" ")   #convert my A vector into a list
    b=B.split(" ")   #convert my B vector into a list
    
    # convert my values in vector A to integers
    list_A=[]
    for i in a:
        i=eval(i)
        list_A.append(i)
        
    #converts my values in vector B to integers   
    list_B=[]
    for i in b:
        i=int(i)
        list_B.append(i)
    
    
    #add my my vectors
    add=[list_A[0]+list_B[0],list_A[1]+list_B[1],list_A[2]+list_B[2]]

    
    #dot product
    cross_product=(list_A[0]*list_B[0]+list_A[1]*list_B[1]+list_A[2]*list_B[2])
    
    
    #norm for vector A
    normA=(list_A[0]**2+list_A[1]**2+list_A[2]**2)
    normA=math.sqrt(normA)
    normA=round(normA,2)

    
    #norm for B
    normB=(list_B[0]**2+list_B[1]**2+list_B[2]**2)
    normB=math.sqrt(normB)
    normB=round(normB,2)
    
    print("A+B =",add)
    print("A.B =",cross_product)
    result="{norm:.2f}"
    print("|A| =",result.format(norm=normA))
    print("|B| =",result.format(norm=normB))
    
    
    

vectors()