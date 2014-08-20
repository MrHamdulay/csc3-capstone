import math

vectorA=input("Enter vector A:\n")
vectorB=input("Enter vector B:\n")

#creating lists
listA=vectorA.split(" ")
listB=vectorB.split(" ")

#Vector multiplication
AB = eval(listA[0])*eval(listB[0])+ eval(listA[1])* eval(listB[1]) + eval(listA[2])*eval(listB[2])

#vector addition
i=eval(listA[0])+eval(listB[0])
j=eval(listA[1])+eval(listB[1])
k=eval(listA[2])+eval(listB[2])

vector_addition=[i,j,k]


# The norm of a single vector 
aA=eval(listA[0])
bA=eval(listA[1])
cA=eval(listA[2])

aB=eval(listB[0])
bB=eval(listB[1])
cB=eval(listB[2])

absA = (math.sqrt(aA**2 + bA**2 + cA**2))
absB = (math.sqrt(aB**2 + bB**2 + cB**2))

formatting = "{0:0.2f}"

print("A+B =",vector_addition)
print("A.B =",AB)
print("|A| =",formatting.format(absA))
print("|B| =",formatting.format(absB))