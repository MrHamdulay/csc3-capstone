import math

vecA=input("Enter vector A:\n").split(" ")

vecB=input("Enter vector B:\n").split(" ")
#variable to hold sum output
sum=[]
# variable to hold product ouput
product=0
#variables to hold mod ouput
normA=0
normB=0
for i in range(len(vecA)):
    #conduct calculations to determine sum, product and mod
    sum.append(eval(vecA[i])+eval(vecB[i]))
    product+=eval(vecA[i])*eval(vecB[i])
    normA+=eval(vecA[i])**2
    normB+=eval(vecB[i])**2
    
#printing output
print("A+B =",sum)
print("A.B =", product)

print("|A| =","{0:.2f}".format(math.sqrt(normA)))
print("|B| =","{0:.2f}".format(math.sqrt(normB)))
