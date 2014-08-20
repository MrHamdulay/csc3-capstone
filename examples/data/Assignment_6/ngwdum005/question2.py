"""Dumisani Ngwenza
21/04/2014
NGWDUM005
Assignment 6 Question 2"""
import math

#creates and stores 2 vectors
vector_A = []
vector_B = []
a = input("Enter vector A:\n")
b = input("Enter vector B:\n")
vector_A = a.split(' ')
vector_B = b.split(' ')

#assigning variables corresponding to the position of the vectors
position_A1 = eval(vector_A[0])
position_A2 = eval(vector_A[1])
position_A3 = eval(vector_A[2])
position_B1 = eval(vector_B[0])
position_B2 = eval(vector_B[1])
position_B3 = eval(vector_B[2])

list_of_numbers = []
#adding 2 vectors
x = position_A1 + position_B1
list_of_numbers.append(x)
y = position_A2 + position_B2
list_of_numbers.append(y)
z = position_A3 + position_B3
list_of_numbers.append(z)
print ('A+B', '=', list_of_numbers)

#dot product: multiplying vectors - the sum of the products of the corresponding elements in the vectors
x = position_A1 * position_B1
y = position_A2 * position_B2
z = position_A3 * position_B3
dot_product = x + y + z
print ('A.B', '=', dot_product)

#normlalisation of vector A
x = position_A1**2
y = position_A2**2
z = position_A3**2
square = math.sqrt(x + y + z)
if square == 0.00:
    print ('|A| = 0.00')
else:
    print ('|A|', '=', round(square, 2))

#normalisation of vector B
x = position_B1**2
y = position_B2**2
z = position_B3**2
square = math.sqrt(x + y + z)
if square == 0.00:
    print ('|B| = 0.00')
else:
    print ('|B|', '=', round(square, 2))

#print (vector_A)

