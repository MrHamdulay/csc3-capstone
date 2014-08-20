#Khyati Jinerdeb
#Assignment 6
#25 April 2014
#program to do basic vector calculations in 3 dimensions

import math     #import maths to do some operations
vectorA=input("Enter vector A:\n")
A=vectorA.split()  #splits the strings into a list
vectorA=[]
for i in A:
    vectorA.append(eval(i))  #add other elements of the list 
    
vectorB=input("Enter vector B:\n")
B=vectorB.split()   #splits the strings into a list
vectorB=[]
for j in B:
    vectorB.append(eval(j))   #add other elements in the list
    
addition=[]
for i in range(len(vectorB)):
    addition.append(vectorA[i]+vectorB[i])   #to add the respective elements of vectors A and B
print("A+B","=", addition)

dotproduct=[]
for j in range(len(vectorB)):
    dotproduct.append(vectorA[j]*vectorB[j])  #to calcualate the product of the respective elements in vectors A and B
    
sum=0
for i in dotproduct:
    sum+=i
print("A.B","=",sum)   #to add all the products in the list dotproduct


#normalisation of vectors
normA=[]
for i in range(len(vectorA)):
    normA.append(vectorA[i]**2)
    i +=1   #loops through and squares each element in the list
    
sum=0    #sum must be initialised to 0
for i in normA:
    sum+=i
print("|A|","=","{0:.2f}".format(math.sqrt(sum)))  #using format to round the value of norm to 2 decimal places

normB=[]
for j in range(len(vectorB)):
    normB.append(vectorB[j]**2)
    j +=1
    
sum=0
for j in normB:
    sum+=j
print("|B|","=","{0:.2f}".format(math.sqrt(sum)))


    
    
    
                                                     
    
    
    





    




    
    






    
    