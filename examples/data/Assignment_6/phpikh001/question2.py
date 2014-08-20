#Ikhlaas Pohplonker
#23 April 214
#a program to do basic vector calculations in 3 dimensions: addition, dot product and normalization
import math

def add(a,b):#returns a list of the sum of corresponding elements
    position=0
    grid=[]
    for i in a:
        grid.append(eval(i)+eval(b[position]))#adds the sum of corresponding elements to the list called grid
        position=position+1
    return grid
def product(a,b):#returns the sum of the products of corresponding elements
    position=0
    sum=0
    for i in a:
        p=eval(i)*eval(b[position])#mutiplies corresponding elements
        sum=sum+p
        position=position+1
    return sum
def norm(a):#returns the square root of the sum of the squares of the elements
    sum=0
    for i in a:
        sum=sum+(eval(i)*eval(i))
    norm=math.sqrt(sum)#square roots the sum of the squares of the elements
    return norm
A=input("Enter vector A:\n").split(" ")
B=input("Enter vector B:\n").split(" ")
print("A+B =", add(A,B))
print("A.B =", product(A,B))
normA = "{0:4.2f}".format(norm(A)) 
normB = "{0:4.2f}".format(norm(B))

print("|A| =", normA)
print("|B| =", normB)