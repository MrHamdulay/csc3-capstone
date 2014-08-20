#ASSIGNMENT 6
#NLTWES001 
#QUESTION 2

A=input("Enter vector A:\n")
A=A.split(" ")
B=input("Enter vector B:\n")
B=B.split(" ")

#addition
addlist=[]
for i in range(3):
    addlist.append(eval(A[i])+eval(B[i]))
print("A+B =",addlist)

#dot product
dotproduct=0
for k in range(3):
    dotproduct+=((eval(A[k]))*(eval(B[k])))
print("A.B =",dotproduct)

#norm
import math
def norm(list):
    sum=0
    for j in range(3):
        sum+=(eval(list[j]))**2
    sum="{:.2f}".format(math.sqrt(sum))
    return(sum)

print("|A| =",norm(A))
print("|B| =",norm(B))
    