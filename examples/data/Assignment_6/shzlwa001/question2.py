# Program for computing vectors
# Lwazi Shezi
# 25 April 2014

import math

# get vectors
print('Enter vector A:')
input_stringA=input()
list_of_A = input_stringA.split()

print('Enter vector B:')
input_stringB=input()
list_of_B = input_stringB.split()


# compute and print the Sum of A and B
sum_AB = 'A+B'
sum_value = '['+str(eval(list_of_B[0])+eval(list_of_A[0]))+", "+str(eval(list_of_B[1])+eval(list_of_A[1]))+", "+str(eval(list_of_B[2])+eval(list_of_A[2]))+']'

print('{0:^3}'.format(sum_AB)+" = "+"{0:<9}".format(str(sum_value)))

# compute and print out the dot product of A and B
product_AB = 'A.B'
product_value = (eval(list_of_B[0])*eval(list_of_A[0]))+(eval(list_of_B[1])*eval(list_of_A[1]))+(eval(list_of_B[2])*eval(list_of_A[2]))



print('{0:^3}'.format(product_AB)+" = "+"{0:<9}".format(str(product_value)))


# Compute and print out norm A
norm_A = '|A|'
norm_A_value = math.sqrt( ((eval(list_of_A[0]))**2)+((eval(list_of_A[1]))**2)+((eval(list_of_A[2]))**2) ) 

print('{0:^3}'.format(norm_A)+" = "+"{0:0<4}".format(str(round(norm_A_value,2))))


# Compute and print out norm B
norm_B = '|B|'
norm_B_value = math.sqrt( ((eval(list_of_B[0]))**2)+((eval(list_of_B[1]))**2)+((eval(list_of_B[2]))**2) ) 

print('{0:^3}'.format(norm_B)+" = "+"{0:0<4}".format(str(round(norm_B_value,2))))


