""" Bella gorham
vectors 
20/04/2014"""

import math
#create empty strings
vectorA = []
vectorB = []

#get input
vectorainput = input("Enter vector A:\n")
#split into the 3 variables
vectora=vectorainput.split()
vectora1 = eval(vectora[0])
vectora2 = eval(vectora[1])
vectora3 = eval(vectora[2])

#add to list
vectorA.append(vectora1)
vectorA.append(vectora2)
vectorA.append(vectora3)

#same for b
vectorbinput = input("Enter vector B:\n")
vectorb=vectorbinput.split()
vectorb1 = eval(vectorb[0])
vectorb2 = eval(vectorb[1])
vectorb3 = eval(vectorb[2])


vectorB.append(vectorb1)
vectorB.append(vectorb2)
vectorB.append(vectorb3)

# adding the 1st,2nd and 3rd terms
sumAB = [(vectorA[0] + vectorB[0]), (vectorA[1] + vectorB[1]), (vectorA[2] + vectorB[2]) ]
# timsing the 1st,2nd and 3rd terms
productAB = (vectorA[0] * vectorB[0])+ (vectorA[1] * vectorB[1])+ (vectorA[2] * vectorB[2]) 

# adding the 1st,2nd and 3rd terms sqaures for a and b    
sumA = vectorA[0]**2 + vectorA[1]**2 + vectorA[2]**2
sumB =  vectorB[0]**2 + vectorB[1]**2 + vectorB[2]**2
# rooting them
normalA = math.sqrt(sumA)
normalB = math.sqrt(sumB)

#printing output
print("A+B =",sumAB)
print("A.B =",productAB)
#format for display
display="|{0}| = {1:0<4}"
print(display.format("A",round(normalA,2)))
print(display.format("B",round(normalB,2)))

