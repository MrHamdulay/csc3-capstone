"""Lenard Carroll
24 April 2014
Assignment 6"""
import math

Vector_A = input("Enter vector A:\n") # User is prompted to enter three values/vectors
Vector_B = input("Enter vector B:\n") # The user is prompted to enter another additional three values/vectors


A_split = Vector_A.split() # This splits the input into different parts (in this case three parts)
B_split = Vector_B.split() # This splits the input into different parts (in this case three parts)

eval_vector_A_1 = eval(A_split[0]) # This converts the value of that certain vector into a useable number
eval_vector_A_2 = eval(A_split[1]) # This converts the value of that certain vector into a useable number
eval_vector_A_3 = eval(A_split[2]) # This converts the value of that certain vector into a useable number

eval_vector_B_1 = eval(B_split[0]) # This converts the value of that certain vector into a useable number
eval_vector_B_2 = eval(B_split[1]) # This converts the value of that certain vector into a useable number
eval_vector_B_3 = eval(B_split[2]) # This converts the value of that certain vector into a useable number

AplusB_1 = (eval_vector_A_1 + eval_vector_B_1)
AplusB_2 = (eval_vector_A_2 + eval_vector_B_2)
AplusB_3 = (eval_vector_A_3 + eval_vector_B_3)

AplusB_1 = round(AplusB_1,2)
AplusB_2 = round(AplusB_2,2)
AplusB_3 = round(AplusB_3,2)

print("A+B ="," [",AplusB_1,", ",AplusB_2,", ",AplusB_3,"]",  sep='')


AdotB = (eval_vector_A_1*eval_vector_B_1) + (eval_vector_A_2*eval_vector_B_2) + (eval_vector_A_3*eval_vector_B_3)
AdotB = round(AdotB,2)

print("A.B =",AdotB)


_A_ = math.sqrt((eval_vector_A_1)**2 + (eval_vector_A_2)**2 + (eval_vector_A_3)**2)
_A_ = "{0:.2f}".format(_A_)

print("|A| =",_A_)

_B_ = math.sqrt((eval_vector_B_1)**2 + (eval_vector_B_2)**2 + (eval_vector_B_3)**2)
_B_ = "{0:.2f}".format(_B_)


print("|B| =",_B_)


