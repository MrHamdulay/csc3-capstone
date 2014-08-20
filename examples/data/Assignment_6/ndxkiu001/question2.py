#Kiuran Naidoo
#Assignment 6
#Question 2
#24 April 2014
import math

vectA = input("Enter vector A:\n").split(" ") #Splitting Input into lists
vectB = input("Enter vector B:\n").split(" ")

for x in range(len(vectA)): #Change inputs from strings to integers
    vectA[x] = eval(vectA[x])
    vectB[x] = eval(vectB[x])

sum = [vectA[0]+vectB[0],vectA[1]+vectB[1],vectA[2]+vectB[2]] #Working out the vector sum
dotProduct = vectA[0]*vectB[0]+vectA[1]*vectB[1]+vectA[2]*vectB[2] #Working out the dot product
normA = math.sqrt(vectA[0]**2+vectA[1]**2+vectA[2]**2) #Working out |A|
normB = math.sqrt(vectB[0]**2+vectB[1]**2+vectB[2]**2)#Working out |B|

#Printing output to user
print("A+B =",sum)
print("A.B =",dotProduct)
print("|A| = {0:.2f}".format(float(normA)))
print("|B| = {0:.2f}".format(float(normB)))
