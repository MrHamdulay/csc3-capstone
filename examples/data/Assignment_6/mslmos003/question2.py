#Rorisang Moseli
#Assignment 6
#Question 2



import math
vector_A = []
vector_B = []
addition = []
dot_product = 0
mod_A_sq = 0
mod_B_sq = 0


vector_A = [int(s) for s in input("Enter vector A:\n").split(" ")]

vector_B = [int(s) for s in input("Enter vector B:\n").split(" ")]


for i in range(len(vector_A)):
    addition += [vector_A[i]+vector_B[i]]
    
for i in range(len(vector_A)):
    dot_product += (vector_A[i]*vector_B[i])
    
for i in range(len(vector_A)):
    mod_A_sq += (vector_A[i]**2)
    
mod_A = round(math.sqrt(mod_A_sq), 2)

for i in range(len(vector_A)):
    mod_B_sq += (vector_B[i]**2)
    
mod_B = round(math.sqrt(mod_B_sq), 2)
    

print ("A+B =",addition)
print ("A.B =",dot_product)
if mod_A == 0.0:
    print ("|A| = 0.00")
else:
    print ("|A| =",mod_A)
    
if mod_B == 0.0:
    print ("|B| = 0.00")
else:
    print ("|B| =",mod_B)