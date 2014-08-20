#Phumelele Ndimande
#Assignment 6

import math

    
#get vectors
vector_A = input("Enter vector A:\n")
vector_B = input("Enter vector B:\n")
vectorA = vector_A.split()
vectorB = vector_B.split()
    
#calculate vector sum
vector_sum= int(vectorA[0])+eval(vectorB[0]) , int(vectorA[1])+int(vectorB[1]),int(vectorA[2])+int(vectorB[2])
listv =list(vector_sum)    #list the sum 
    
print("A+B =", listv)
    
#calclate dot product
dot_product= (int(vectorA[0])*int(vectorB[0])) + (int(vectorA[1]) * int(vectorB[1])) +(int(vectorA[2]) *int(vectorB[2]))
    
print("A.B =", dot_product)
    
#calculate normal
normalA = round(math.sqrt((int(vectorA[0])**2) + (int(vectorA[1])**2) + (int(vectorA[2])**2)),2)
if normalA != 0.0:
    print("|A| =", normalA)
else:
    print("|A| = 0.00")
    
normalB =round(math.sqrt((int(vectorB[0])**2) + (int(vectorB[1])**2) + (int(vectorB[2])**2)),2)
if normalB != 0.0:
    print("|B| =", normalB)  
else:
    print("|B| = 0.00")
    
