#Assignment 6
#By: Litha Maqungo
#24 April 2014
import math
vector_a=[]
vector_b=[]
vector_add=[]
total=0
squared_total = 0
squared_total2 = 0
A=input("Enter vector A: \n")#input for A
vector_a.append(A)
A.split(' ')
B=input("Enter vector B: \n")#input for B
vector_b.append(B)
B.split(' ')
for i in range(0,5,2): #allows the calculation for the sum of the individual vectors 
    z= int(A[i]) + int(B[i])
    vector_add.append(z) #added to the list of vectors overall
print("A+B = ", vector_add, sep ='')
for j in range (0,5,2):
    y= int(A[j])* int(B[j])
    total= total + y
print("A.B = ", total,sep='') #the dot product is printed
for k in range(0,5,2):
    squared= int(A[k])**2
    squared_total= squared_total + squared 
print("|A| =", round(math.sqrt(squared_total),2)) #gets the square root of the total sum
for l in range(0,5,2):
    squared= int(B[l])**2
    squared_total2= squared_total2 + squared
print("|B| =", round(math.sqrt(squared_total2),2))



    



