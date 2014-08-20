"""Assignment 6 Q2-Vectors
Nandani Birjanund
23/04/14"""

import math #Math library

list1=[]

a=input("Enter vector A:\n") #User inputs
b=input("Enter vector B:\n")      

vectA=a.split(" ")  #splits string into individual number (1, 2 etc) and adds it to the array
vectB=b.split(" ")

for i in range (3): #Add items in vectors A,B insert new array
    
    add=int(vectA[i])+int(vectB[i]) #add vect
    list1.append(add)#adds to array 

print("A+B =",list1) #prints out inputs and list1

sum=0

for j in range(3): #calculates the sum of products
    product=int(vectA[j])*int(vectB[j]) #multiplies vect
    sum+=product
    
    
print("A.B =",sum) #to calculate the norm
sqA=0
sqB=0

for k in range (3): #loop for norm
# loop finding norm of A
    
    squareA=int(vectA[k])*int(vectA[k])
    sqA+=squareA
    normA=math.sqrt(sqA) #math function to get square root
# loop finding norm of B    
    squareB=int(vectB[k])*int(vectB[k])
    sqB+=squareB
    normB=math.sqrt(sqB)  #math function to get square root   
#printing the norm
normfA="{0:.2f}".format(normA)
normfB="{0:.2f}".format(normB)
print("|A| =",normfA)
print("|B| =",normfB)