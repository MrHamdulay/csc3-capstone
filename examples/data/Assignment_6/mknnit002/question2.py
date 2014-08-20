#mknnit002
#question 2 ass 6

A=[]
B=[]     #create empty lists
x=[]
y=[]
t=[]
z=[]

vector_A=input("Enter vector A:\n")
A=vector_A.split(" ")

vector_B=input("Enter vector B:\n")    #get input from users and split 
B=vector_B.split(" ")

for i in range(3):
    x.append(eval(A[i])+eval(B[i]))    #sum of vectors
    
print("A+B=",x)

for i in range(3):
    y.append(eval(A[i])*eval(B[i]))       # dot function

print("A.B=",y)   

import math 
for i in range(3):
    z.append(math.sqrt(eval(A[i])**2))     #sqrt function vector A
    
print("|A|=",z)

for i in range(3):
    t.append(math.sqrt(eval(B[i])**2))   #sqrt function vector B
             
print("|B|=",t)

            
    
    


