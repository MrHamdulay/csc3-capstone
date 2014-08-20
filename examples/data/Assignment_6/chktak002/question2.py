import math
a=input("Enter vector A:\n")
b=input("Enter vector B:\n")
A=[] #creates an empty list

B=[] #creates an empty list

        
for num in a.split(): # enters each number seperated by a space into a sepeate index
        num =eval(num)   
        
        A.append(num) # adds items entered to the list
    
for num in b.split(): # enters each number seperated by a space into a sepeate index
        num=eval(num)
        
        B.append(num) #adds items entered to thelist


print("A+B =",[(A[0]+B[0]),(A[1]+B[1]),(A[2]+B[2])])  

print("A.B =",(A[0]*B[0]+A[1]*B[1]+A[2]*B[2]))

square_root=math.sqrt(A[0]**2+A[1]**2+A[2]**2)
if square_root==0.0:
        print("|A| = 0.00")
else:
        print("|A| =",round(square_root,2))
                          
square_root=math.sqrt(B[0]**2+B[1]**2+B[2]**2)
if square_root==0.0:
        print("|B| = 0.00")
else:
        print("|B| =",round(square_root,2))    
             

