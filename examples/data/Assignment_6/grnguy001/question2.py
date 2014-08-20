#Done By Guy Green
#Dot Product, adding vectors and working out magnitude of vectors
#For assignment 6

import math

#Getting vector from user
VectorA=input("Enter vector A:\n")
VectorB=input("Enter vector B:\n")

#Seperating the numbers of the vectors
VectorA=VectorA.split(" ")
VectorB=VectorB.split(" ")


#Might NOT work for boundary cases

#Working out dot product by multiplying each of the like components and adding it to original 0
dotAB=0
for i in range(len(VectorA)):
    ComponentA=VectorA[i] #x,y and z components
    ComponentB=VectorB[i] #x,y and z components
    dotAB+=eval(ComponentA)*eval(ComponentB)

#Creating a list because it is easier to print required output
sumAB=[]
for j in range(len(VectorA)):
    ComponentA=VectorA[j]
    ComponentB=VectorB[j]
    ABadded=str(eval(ComponentA)+eval(ComponentB)) #adding the components as strings so they don't add different components of the vector
    sumAB.append(int(ABadded)) #Adding to list

#Working out magnitude by adding the square of the  components and and then squarerooting the sum 
magAsquared=0.00
magBsquared=0.00

for k in range(len(VectorA)):
    ComponentA=VectorA[k]
    ComponentB=VectorB[k]
    magAsquared+=(eval(ComponentA))**2 #Squaring each component
    magBsquared+=(eval(ComponentB))**2 #Squaring each component
      
#Squarerooting it and rounding it off to two decimal places
magA=math.sqrt(magAsquared)
magA=round(magA, 2)

magB=math.sqrt(magBsquared)
magB=round(magB, 2)

#If it an actual integer is the answer, python only gives one decimal place. This is to add a decimal place
if len(str(magA))==3:
    magA=str(magA)+"0"
if len(str(magB))==3:
    magB=str(magB)+"0"

#Printing
print("A+B =", sumAB)
print("A.B =", dotAB)
print("|A| =", magA)
print("|B| =", magB)