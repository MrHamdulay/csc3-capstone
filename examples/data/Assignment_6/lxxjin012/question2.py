#a program to do basic vector calculations in 3 dimensions:
#Jenny Luo
#23 April 2014

import math

def main():
    #add element into list VectA
    A=input("Enter vector A:\n")
    A=A.split()#can only split a string, not a number
    VectA=[]
    for i in A:
        VectA.append(eval(i))
    
    #add element into list VectB
    B=input("Enter vector B:\n")
    B=B.split()#can only split a string, not a number
    VectB=[]
    for j in B:
        VectB.append(eval(j)) 
    
    #sum of the vectors
    Addition=[]
    for i in range(len(VectA)):
        Addition.append(VectA[i]+VectB[i])
    print("A+B","=", Addition)
    
    #dot product of the vectors
    product=[]
    for i in range(len(VectA)):
        product.append(VectA[i]*VectB[i])
    sum=0
    for i in product:
        sum+=i
    print("A.B","=",sum)
    
    #normalisation of vector
    normA=[]
    for i in range(len(VectA)):
        normA.append(VectA[i]**2)
        i +=1
    sum=0
    for i in normA:
        sum+=i
    print("|A|","=", "{0:.2f}". format(math.sqrt(sum)))
    
    #normalisation of vector
    normB=[]
    for i in range(len(VectB)):
        normB.append(VectB[i]**2)
        i +=1
    sum=0
    for i in normB:
        sum+=i
    print("|B|","=", "{0:.2f}".format(math.sqrt(sum)))    
main()