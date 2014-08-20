#-------------------------------------------------------------------------------
# A program that compute basic vector operations on two 3 * 3 vectors.
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011
#-------------------------------------------------------------------------------

import math         # Make the math module available.

def main(): 
    # Prompt the user for input of two vectors.
    A = input("Enter vector A:\n")
    B = input("Enter vector B:\n")
    
    # Split the strings and assign them to a list.
    A = A.split()
    B = B.split()
    
    # Convert the strings in the the list to numeric data.
    x1 = eval(A[0])
    y1 = eval(A[1])
    z1 = eval(A[2])
    x2 = eval(B[0])
    y2 = eval(B[1])
    z2 = eval(B[2])
    
    # Compute vector operations.
    summation = [x1 + x2, y1 + y2, z1 + z2 ]
    dot = (x1 * x2) + (y1 * y2) + (z1 * z2)
    magnitude_A = math.sqrt((x1 ** 2) + (y1 ** 2) + (z1 ** 2))
    magnitude_B = math.sqrt((x2 ** 2) + (y2 ** 2) + (z2 ** 2))
    
    # Display the results.
    print("A+B =", summation)
    print("A.B =", dot)
    print("|A| =", format(magnitude_A, ".2f"))
    print("|B| =", format(magnitude_B, ".2f"))
    
# Call the main function.
main()