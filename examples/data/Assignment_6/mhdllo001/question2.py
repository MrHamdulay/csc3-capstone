import math

a_norm = 0 

b_norm = 0 

sum = [ ]

dot = 0

a=input("Enter vector A:\n")

b= input("Enter vector B:\n")

A = a.split()

B = b.split()


j=0
while(j<len(A)):
    A[j] = eval(A[j])
    B[j] = eval(B[j])    
    
    a_norm =a_norm + (A[j])**2
    b_norm =b_norm + (B[j])**2  
   

    sum.append(A[j] + B[j])
    dot += A[j]*B[j]
  
    j=j+1
print ("A+B =", sum)

print ("A.B =", dot)

print("|A| =", round(math.sqrt(a_norm),2))

print("|B| =", round(math.sqrt(b_norm),2))