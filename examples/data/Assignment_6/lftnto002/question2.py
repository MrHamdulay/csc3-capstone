"""Program that does basic vector calculations in 3 dimensions
   Bridgette Lefatsa
   LFTNTO002
   24 April  2014"""

import math

#input from user into arrays

#VectorA
stringA= input("Enter vector A:\n")
VectorA=[]
for x in stringA.split(" "):
    VectorA.append(x)
    
#VectorB
stringB= input("Enter vector B:\n")
VectorB=[]
for x in stringB.split(" "):
    VectorB.append(x)
    
#Addition A+B=C
VectorC=[]
for i in range(3):
    k=eval(VectorA[i])+eval(VectorB[i])
    VectorC.append(k)
print("A+B =",VectorC)

#Dot product
sum_product=0
for i in range(3):
    k=eval(VectorA[i])*eval(VectorB[i])
    sum_product=sum_product+k
print("A.B =",sum_product)

def normalization(vector):
    sum_vector=0
    count=0
    for i in vector:
        count+=eval(i)
    if count==0:
        return  "0.00"
    else:   
        for x in vector:
            sum_vector+=(eval(x)**2)
        
        return round(math.sqrt(sum_vector),2)
    
            

print("|A| =",normalization(VectorA))
print("|B| =",normalization(VectorB))