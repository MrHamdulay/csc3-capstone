"""" Tumi Mkhawana
24 April 2014
Question 2"""

import math

#ask user for input
vector_A =input("Enter vector A:\n")
vector_B =input("Enter vector B:\n")

#changing inputs into to string
listA= vector_A.split(" ")
listB= vector_B.split(" ")

total= []
product=[]
for i in range (len(listA)):
    for j in range (len(listB)):
        if i==j:
            total.append((eval(listA[i])+eval(listB[i])))
            product.append(((eval(listA[i])*eval(listB[i]))))
            
squareA= []
squareB= []
for i in range(len(listA)):
    squareA.append(eval(listA[i])**2)
for j in range(len(listB)):
    squareB.append(eval(listB[j])**2)
    
addzeroA="{0:.2f}".format(math.sqrt(sum(squareA)))
addzeroB="{0:.2f}".format(math.sqrt(sum(squareB)))

print("A+B =",total)
print("A.B =",sum(product))
print("|A| = ",addzeroA,sep="")
print("|B| = ",addzeroB,sep="")