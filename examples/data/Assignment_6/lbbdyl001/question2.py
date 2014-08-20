"""
Basic Vector Calculations
"""
import math

input_a = input("Enter vector A:\n")
input_b = input("Enter vector B:\n")

vector_a = input_a.split() #split string by space
vector_b = input_b.split()

add = [ ]
product = 0
a_norm = 0 
b_norm = 0 

for num in range(3): #max is 3 components 
    vector_a[num] = eval(vector_a[num]) #conversion into integer
    vector_b[num] = eval(vector_b[num])
    
    add.append(vector_a[num] + vector_b[num]) #addition of corresponding vector components
    
    product += (vector_a[num]*vector_b[num]) #product of corresponding vector components
    
    a_norm += ((vector_a[num])**2) #sum of square of each component
    b_norm += ((vector_b[num])**2)
    
print ("A+B =", add)
print ("A.B =", product)

if a_norm>0:
    print ("|A| =", round(math.sqrt(a_norm),2)) 
else:
    print("|A| = 0.00")
    
if b_norm>0:
    print ("|B| =", round(math.sqrt(b_norm),2))
else:
    print("|B| = 0.00")
