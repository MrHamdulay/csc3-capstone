# question2.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 23 April 2014

A=input("Enter vector A:\n")
A_list=A.split(" ")                         #split input A into list
B=input("Enter vector B:\n")
B_list=B.split(" ")                         #split input B into list

addition=[]                                 #create empty list of addition outcomes
for i in range(3):
    A=eval(A_list[i])                       #convert inputs in list A into integers
    B=eval(B_list[i])                       #convert inputs in list B into integers
    add=A+B                                 #sum corressponding A and B variables from list A and list B
    addition.append(add)                    #append the result of the summation to list of addition outcomes

product=0
for j in range(3):
    A=eval(A_list[j])                       #convert inputs in list A into integers
    B=eval(B_list[j])                       #convert inputs in list B into integers
    multiply=A*B                            #multiply corresponding A and B variables from list A and list B
    product+=multiply                       #sum products

import math
sum_A=0
for k in range(3):
    A=eval(A_list[k])                       #convert inputs in list A into integers
    sum_A+=A**2                             #sum of the squares of inputs in list A
abs_A=math.sqrt(sum_A)                      #root of the sum of the squares of inputs in list A
answer_A=round(abs_A,2)                     #round answer to two decimal places
if answer_A==0.0:
    answer_A=str(answer_A)+'0'
sum_B=0
for l in range(3):
    B=eval(B_list[l])                       #convert inputs in list B into integers
    sum_B+=B**2                             #sum of the squares of inputs in list B
abs_B=math.sqrt(sum_B)                      #root of the sum of the squares of inputs in list B
answer_B=round(abs_B,2)                     #round answer to two decimal places
if answer_B==0.0:
    answer_B=str(answer_B)+'0'

#print results
print("A+B =",addition)
print("A.B =",product)
print("|A| =",answer_A)
print("|B| =",answer_B)