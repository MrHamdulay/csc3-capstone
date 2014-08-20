"""Program to do basic vector culculations
Roger Cox
23/04/2014"""
import math
# so you can use sqrt etc

def add (A,B):
    add=[]
    for i in range(3):
        add.append(eval(A[i])+eval(B[i]))
    
    print("A+B =",add)
# addition    
def multiply (A,B):
    
    multiply=0
    for i in range(3):
        multiply+=(eval(A[i])*eval(B[i]))  
        
        
    print("A.B =",multiply)
    
    
def sqrt (A):
    sq=0
    for i in range(3):
        sq+=eval((A[i]))**2   
    x=((sq**0.5))
    return x

# sqrt used for both a and b
vector_a=input("Enter vector A:\n")
A=vector_a.split(" ")
# get vector a
vector_b=input("Enter vector B:\n")
B=vector_b.split(" ")
# get vector B
add(A,B) 

multiply(A,B)
b="|A| = {a:0.2f}"
c="|B| = {a:0.2f}"
print(b.format(a=sqrt(A)))

print(c.format(a=sqrt(B)))

#print (add)