"""Vector calculations
danica van der zandt
24 april 2014"""

import math

#get vector inputs from the user and store them as a list
A=input("Enter vector A:\n")
vector_A=A.split()

B=input("Enter vector B:\n")
vector_B=B.split()


#addition of vectors
#using a_value where a is for "adding"
adding=[]
a_first=int(vector_A[0])+int(vector_B[0])
adding.append(a_first)
a_second=int(vector_A[1])+int(vector_B[1])
adding.append(a_second)
a_third=int(vector_A[2])+int(vector_B[2])
adding.append(a_third)
print("A+B =",adding)



#dot product
#using d_value where d is for "dot production"
dotpro=[]
d_first=int(vector_A[0])*int(vector_B[0])
dotpro.append(d_first)
d_second=int(vector_A[1])*int(vector_B[1])
dotpro.append(d_second)
d_third=int(vector_A[2])*int(vector_B[2])
dotpro.append(d_third)
final_dotpro=int(dotpro[0])+int(dotpro[1])+int(dotpro[2])

print("A.B =",final_dotpro)

#norm of A
integers=[]
sqrd_integers=[]
#getting a list of integers
for numbers in vector_A:
    integers.append(int(numbers))

#squaring the integers in "integers"    
for sqrd in integers:
    sqrd_integers.append(int(sqrd)**2)
    
#adding the squared numbers
add_sqrd=int(sqrd_integers[0]+sqrd_integers[1]+sqrd_integers[2])

#square root of add_sqrd rounded off to two decimal places
final_norm_A= "%2.2f" % math.sqrt(add_sqrd)
print("|A| =", final_norm_A)


#norm of B
integers=[]
sqrd_integers=[]
#getting a list of integers
for numbers in vector_B:
    integers.append(int(numbers))

#squaring the integers in "integers"    
for sqrd in integers:
    sqrd_integers.append(int(sqrd)**2)
    
#adding the squared numbers
add_sqrd=int(sqrd_integers[0]+sqrd_integers[1]+sqrd_integers[2])

#square root of add_sqrd rounded off to two decimal places
final_norm_B= "%2.2f" % math.sqrt(add_sqrd)
print("|B| =", final_norm_B)