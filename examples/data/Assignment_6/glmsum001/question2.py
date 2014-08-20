#GLMSUM001
#Sumayah Goolam Rassool
#23 April 2014

import math

#------------------------------input into vectors
list1=[]


a=input("Enter vector A:\n")
b=input("Enter vector B:\n")
#s----------------------------split string into individual number and add into array
vectA=a.split(" ")
vectB=b.split(" ")
#-----------------------------add items in vector A and vector B and insert into new array
for i in range (3):
    
    add=int(vectA[i])+int(vectB[i])
    list1.append(add)

print("A+B =",list1)

#----------------------------dot.product

sum=0
#----------------------------calculate sum of products
for j in range(3):
    product=int(vectA[j])*int(vectB[j])
    sum+=product
    
    
print("A.B =",sum)

#---------------------------calculate norm
sqA=0
sqB=0

for k in range (3):

#--------------------------finding norm of A
    
    squareA=int(vectA[k])*int(vectA[k])
    sqA+=squareA
    normA=math.sqrt(sqA)
#-------------------------finding norm of B    
    squareB=int(vectB[k])*int(vectB[k])
    sqB+=squareB
    normB=math.sqrt(sqB)    
#------------------------printing norm
normfA="{0:.2f}".format(normA)
normfB="{0:.2f}".format(normB)
print("|A| =",normfA)
print("|B| =",normfB)

    
   
    