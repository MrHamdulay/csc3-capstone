"""Cherise Dube
19 April 2014
Program to do basic vector calculations in 3 dimensions: addition, dot product and normalization."""

vectorA=(input("Enter vector A:\n")).split(" ")
vectorB=(input("Enter vector B:\n")).split(" ")

#Adds the elements of each vector that are in the same position creating a new vector
add_AB=[]
for i in range(3):
    addition=int(vectorA[i])+int(vectorB[i])
    add_AB.append(addition)

print("A+B =",add_AB)

#Multiplies elements of a vector in the same position and adds everything together
dot_product_addition=0
for i in range(3):
    dot_product=(int(vectorA[i]))*(int(vectorB[i]))
    dot_product_addition+=dot_product
    
print("A.B =",dot_product_addition)

#Finds the norm of a single vector (i.e. the square root of the sum of the squares of each vector)
#vectorA
import math
sum_of_squares=0
for i in range(3):
    square=(int(vectorA[i]))**2
    sum_of_squares+=square
    
print("|A| =",'%.2f'%math.sqrt(sum_of_squares))
      
#vectorB

sum_of_squares=0
for i in range(3):
    square=(int(vectorB[i]))**2
    sum_of_squares+=square
    
    
print("|B| =",'%.2f'%math.sqrt(sum_of_squares))

