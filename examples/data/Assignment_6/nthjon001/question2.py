"""program which computes basic 3D vector properties
Jonathan Nathan
20 April 2014"""

# import math module in order to utilise the square root function
import math

# gets vector A from user and converts input to a list
vectorA_input = input("Enter vector A:\n")
vectorA_list = vectorA_input.split(' ')

# gets vector B from user and converts input to a list
vectorB_input = input("Enter vector B:\n")
vectorB_list = vectorB_input.split(' ')

# calculates addition of two vectors by adding items in both of the two lists above
sum_result = [eval(vectorA_list[0]) + eval(vectorB_list[0]), eval(vectorA_list[1]) + eval(vectorB_list[1]), eval(vectorA_list[2]) + eval(vectorB_list[2])]

# calculates the dot product of the two vectors by adding the individual products of values in the above two lists in the same index
dot_product_result = (eval(vectorA_list[0]) * eval(vectorB_list[0])) + (eval(vectorA_list[1]) * eval(vectorB_list[1])) + (eval(vectorA_list[2]) * eval(vectorB_list[2]))

# calculates the norm of vector A by squaring each component in the vectorA_list and adding these
normA_result = math.sqrt((eval(vectorA_list[0]) **2) + (eval(vectorA_list[1]) **2) + (eval(vectorA_list[2]) **2))

# calculates the norm of vector B by squaring each component in the vectorB_list and adding these
normB_result = math.sqrt((eval(vectorB_list[0]) **2) + (eval(vectorB_list[1]) **2) + (eval(vectorB_list[2]) **2))

# prints the sum, dot product, norm of A and norm of B calculated above
print('A+B =', sum_result)
print('A.B =', dot_product_result)
# format ensures that the norms are given to 2 decimal places
print('|A| =', '{0:0.2f}'.format(normA_result))
print('|B| =', '{0:0.2f}'.format(normB_result))