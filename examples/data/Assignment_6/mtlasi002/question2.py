#Asil Motala
#MTLASI002
#Assignment 6
#Question 2

A=input("Enter vector A:\n")                #get input from user
A_list=A.split(" ")                         #split input A into list
B=input("Enter vector B:\n")                #get input from user
B_list=B.split(" ")                         #split input B into list

addition=[]                                 #initialize list of addition outcomes
for i in range(3):
    A=eval(A_list[i])                       #convert list A inputs into integers
    B=eval(B_list[i])                       #convert list B inputs into integers
    add=A+B                                 #add corresponding A and B variables from lists
    addition.append(add)                    #add result to list of addition outcomes

product=0                                   #initialize product variable
for j in range(3):
    A=eval(A_list[j])                       #convert list A inputs into integers
    B=eval(B_list[j])                       #convert list B inputs into integers
    multiply=A*B                            #multiply corresponding A and B variables from lists
    product+=multiply                       #sum products of corresponding variables

import math                                 #import math library
sum_A=0                                     #initialize variable
for k in range(3):
    A=eval(A_list[k])                       #convert list A inputs into integers
    sum_A+=A**2                             #sum the squares of list A inputs
abs_A=math.sqrt(sum_A)                      #find the root of the sum of the squares of list A inputs
answer_A=round(abs_A,2)                     #round answer to two decimal places
if answer_A==0.0:
    answer_A=str(answer_A)+'0'
sum_B=0                                     #initialize variable
for l in range(3):
    B=eval(B_list[l])                       #convert list B inputs into integers
    sum_B+=B**2                             #sum the squares of list B inputs
abs_B=math.sqrt(sum_B)                      #find the root of the sum of the squares of list B inputs
answer_B=round(abs_B,2)                     #round answer to two decimal places
if answer_B==0.0:
    answer_B=str(answer_B)+'0'

print("A+B =",addition)                     #print addition result
print("A.B =",product)                      #print product result
print("|A| =",answer_A)                     #print normal result A
print("|B| =",answer_B)                     #print normal result B