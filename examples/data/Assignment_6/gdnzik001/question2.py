"""program to do basic vector calculations in 3 dimensions
Zikho Godana
23 april 2014"""

import math

#create empty lists
vectorA=[]
vectorB=[]
sums=[]
products=[]
squaresA=[]
squaresB=[]

vectorA=input("Enter vector A:\n")
vectorB=input("Enter vector B:\n")

#ensure that the vectors are stored as a list
list1=vectorA.split()
list2=vectorB.split()

#iterate over each item in the list
for i in range(len(list1)):
    sum=int(list1[i])+int(list2[i])
    sums.append(sum)
    product=int(list1[i])*int(list2[i])
    products.append(product)
    squareA=int(list1[i])**2
    squareB=int(list2[i])**2
    squaresA.append(squareA)
    squaresB.append(squareB)
    
    
sum_squaresA=squaresA[0]+squaresA[1]+squaresA[2] 
sum_squaresB=squaresB[0]+squaresB[1]+squaresB[2]
norm_A = math.sqrt(sum_squaresA)
norm_B = math.sqrt(sum_squaresB)
output="{name:.2f}"#format the dot products to 2 decimal places
print("A+B =",sums)
print("A.B =",products[0]+products[1]+products[2])
print("|A| =",output.format(name=norm_A))
print("|B| =",output.format(name=norm_B))
