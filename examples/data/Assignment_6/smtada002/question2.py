'''Assignment 6 question 2 Vector calculations
Adam Smith
23 April 2014'''

import shlex 
import math

A = shlex.split(input("Enter vector A:\n")) #gets the values inputted for the vectors and stores them in a list
B = shlex.split(input("Enter vector B:\n"))

#does the calculation with the values in the lists and prints out the answers in the correct format
print("A+B = [" + str(int(A[0]) + int(B[0])) + ", "  + str(int(A[1]) + int(B[1])) + ", "  + str(int(A[2]) + int(B[2])) + "]")
print("A.B = " + str(int(A[0])*int(B[0]) + int(A[1])*int(B[1]) + int(A[2])*int(B[2])))
print("|A| = " + '{:.2f}'.format(round(math.sqrt(int(A[0])**2 + int(A[1])**2 + int(A[2])**2),2)))
print("|B| = " + '{:.2f}'.format(round(math.sqrt(int(B[0])**2 + int(B[1])**2 + int(B[2])**2),2)))