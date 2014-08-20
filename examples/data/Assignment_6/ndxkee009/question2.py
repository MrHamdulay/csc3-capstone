"""Keegan Naidoo
NDXKEE009
20 April 2014"""

import math
from decimal import Decimal

A=[]   # Create list for vectors A                                         
B=[]   # Create list for vectors B

A=input("Enter vector A:\n").split(" ")      #Inputs vectors A
B=input("Enter vector B:\n").split(" ")      #Inputs vectors A

#print(A[0],B[0])

print("A+B = [", int(A[0])+int(B[0]),", ", int(A[1])+int(B[1]),", ", int(A[2])+int(B[2]),"]",sep='')   #Calculates and prints addition of vectors

print("A.B = ",(int(A[0])*int(B[0]))+((int(A[1]))*int(B[1]))+((int(A[2]))*int(B[2])),sep='')#Calculates and prints dot product of vectors

a_norm1= (float(A[0]))**2        #Calculates and Converts the norm of vector A at position 1 to a float
a_norm2= (float(A[1]))**2        #Calculates and Converts the norm of vector A at position 1 to a float
a_norm3= (float(A[2]))**2        #Calculates and Converts the norm of vector A at position 1 to a float 

a_norm=a_norm1+a_norm2+a_norm3   #Calculates the total norm of vector A from all positions

print("|A| = %.2f"%(round(math.sqrt((a_norm)),2)),sep='')    #Calculates and prints the norm of vector A

print("|B| = %.2f"%(round(math.sqrt(((int(B[0]))**2)+((int(B[1]))**2)+((int(B[2]))**2)),2)),sep='') #Calculates and prints the norm of vector B

#a="10.0"

#print(Decimal(a)**1)

#print(math.sqrt(14))