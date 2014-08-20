#vector calculations
#julia breakey
#21 april 2014

#input vectors
strA=input("Enter vector A: \n")
A=strA.split(" ")
strB=input("Enter vector B: \n")
B=strB.split(" ")

#add vectors
one = eval(A[0]) + eval(B[0])
two = eval(A[1]) + eval(B[1])
three = eval(A[2]) + eval(B[2])
added = [one, two, three]

#product of vectors
a=eval(A[0])*eval(B[0])
b=eval(A[1])*eval(B[1])
c=eval(A[2])*eval(B[2])
product=a+b+c

#norm of A
import math
norm=0
for i in range(len(A)):
    x=eval(A[i])**2
    norm+=x
normA=math.sqrt(norm)

#norm of B
import math
normB=0
for i in range(len(B)):
    x=eval(B[i])**2
    normB+=x
normB=math.sqrt(normB)

#final print
print("A+B", "=", added)
print("A.B", "=", product)
print("|A|", "=", "{:.2f}".format(normA))
print("|B|", "=", "{:.2f}".format(normB))