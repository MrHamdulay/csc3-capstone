"""A program to do basic 3D vector calculations
Alison Hoernle
HRNALI002
20 April 2014"""

# function to add
def add(A, B):
    first_item = str(eval(A[0]) + eval(B[0]))
    second_item = str(eval(A[1]) + eval(B[1]))
    third_item = str(eval(A[2]) + eval(B[2]))
    add_str = '[' + first_item + ', ' + second_item + ', ' + third_item + ']'
    print('A+B =', add_str)

# function to do dot product    
def dot(A, B):
    first_item = eval(A[0]) * eval(B[0])
    second_item = eval(A[1]) * eval(B[1])
    third_item = eval(A[2]) * eval(B[2])
    dot_product = first_item + second_item + third_item
    print('A.B =', dot_product)
    
# function to do normalization
def normalization(x):
    import math
    first = eval(x[0])
    second = eval(x[1])
    third = eval(x[2])
    norm = math.sqrt(first**2 + second**2 + third**2) # formula for normalization
    
    norm_round = "{0:.2f}".format(norm) # round to 2 decimal places
    if x is A:
        print('|A| =', norm_round)
    else:
        print('|B| =', norm_round)
    

# Get vector A and turn it into a list
vecA_str = input("Enter vector A:\n")
A = vecA_str.split()
    
# Get vector B and turn it into a list
vecB_str = input("Enter vector B:\n")
B = vecB_str.split()

add(A, B)
dot(A, B)
normalization(A)
normalization(B)
