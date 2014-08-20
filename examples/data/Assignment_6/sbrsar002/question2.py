"""a program to do basic vector calculations
Sarayn Subroyen
21 april 2014"""
import math
#change vector(string) into list

listA=input("Enter vector A:\n")
A=listA.split()

listB=input("Enter vector B:\n")
B=listB.split()

#sum of vectors
#a2=print(eval(listA[2]))...tracing
#b2=print(eval(listB[2]))...tracing   
#c1=(eval(listA[0])+eval(listB[0]))
#c2=(eval(listA[2])+eval(listB[2]))
#c3=(eval(listA[4])+eval(listB[4]))
sum_vector=[int(A[0])+int(B[0]),int(A[1])+int(B[1]),int(A[2])+int(B[2])]

print("A+B =",sum_vector)


#dot product
#dp1=(eval(listA[0]))*(eval(listB[0]))
#dp2=(eval(listA[2]))*(eval(listB[2]))
#dp3=(eval(listA[4]))*(eval(listB[4]))
dp=int(A[0])*int(B[0])+int(A[1])*int(B[1])+int(A[2])*int(B[2])
print("A.B =",dp)

#normalize vector A
#a1=eval(listA[0])**2
#a2=eval(listA[2])**2
#a3=eval(listA[4])**2
a=math.sqrt(int(A[0])**2 +int(A[1])**2 +int(A[2])**2)
print("|A| =","{0:.2f}".format(a))  #format to 2 decimal places

#normalize vector B
#b1=eval(listB[0])**2
#b2=eval(listB[2])**2
#b3=eval(listB[4])**2
b=math.sqrt(int(B[0])**2 +int(B[1])**2 +int(B[2])**2)
print("|B| =","{0:.2f}".format(b))

#green code does not run for negative numbers