"""Aiden Walton
WLTAID001
Assignment 6 - question 2"""
import math
#Ask user for input and process vector into array
vectorA=input("Enter vector A:\n")
vectorB=input("Enter vector B:\n")
array1=vectorA.split(" ")
array2=vectorB.split(" ")
#process vectors
addition=[]
def add():
    array1=vectorA.split(" ")
    array2=vectorB.split(" ")    
    for x in range(len(array1)):
        for y in range(len(array2)):
            if x==y:
                add=int(array1[x])+int(array2[y])
                addition.append(add)

def multiply():
    array1=vectorA.split(" ")
    array2=vectorB.split(" ")
    ans=0
    for x in range(len(array1)):
        for y in range(len(array2)):
            if x==y:
                anstemp=int(array1[x])*int(array2[y])
                ans+=anstemp
            else:
                continue
    return ans
def norm(x):
    ans1=0
    for i in range(len(x)):
        ans1+=int(x[i])**2
    return math.sqrt(ans1)

ans_add=add()
ans_mul=multiply()
print("A+B =", addition)
print("A.B =", ans_mul)
print("|A| =", "{:.2f}".format(round(norm(array1),2)))
print("|B| =", "{:.2f}".format(round(norm(array2),2)))



        
#print three calculations
