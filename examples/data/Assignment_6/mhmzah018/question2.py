"""Assignment 6 - question 2
Zaheer Mahmood
20 - 04 - 2014"""

import math
#create array to store vectors
vector_a=[]
vector_b=[]
vector_ad = []


#get input from user
answer_a = input("Enter vector A:\n")
vector_a = answer_a.split(" ")

answer_b = input("Enter vector B:\n")
vector_b = answer_b.split(" ")

#construct loop to allow for manipulation
total_pro=0
total_norm_a=0
total_norm_b=0
for i in range(len(vector_a and vector_b)):
       
# convert list string values into number values
    manipulation_a = eval(vector_a[i])
    manipulation_b = eval(vector_b[i])
    addition = manipulation_a + manipulation_b
    product = manipulation_a * manipulation_b
    
# add values to the list that represents addition
    vector_ad.append(addition)
    
#create counter to add products
    total_pro += product
    
#create counter to add squares
    norm_a = manipulation_a**2
    total_norm_a+=norm_a
    
    norm_b = manipulation_b**2
    total_norm_b+=norm_b
#format string correct to two decimal places
total_norm_a_final = "%.2f" %(math.sqrt(total_norm_a))
total_norm_b_final = "%.2f" %(math.sqrt(total_norm_b))

print("A+B =", vector_ad)
print("A.B =", total_pro)
print("|A| =", total_norm_a_final)
print("|B| =", total_norm_b_final)

