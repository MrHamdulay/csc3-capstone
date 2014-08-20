'''
Prashanth Sridharan
SRDPRA001
Assignment 06
Question 02
'''
import math

def vector_sum (A, B): # User defined class for summing up the input vectors
   return [A[0]+B[0], A[1]+B[1], A[2]+B[2]]
   
def vector_product (A, B): # User defined class for multiplying up the input vectors
   return A[0]*B[0] + A[1]*B[1] + A[2]*B[2] 
   
def vector_norm (A): # User defined class for finding the norm to the input vectors
   return math.sqrt (A[0]*A[0] + A[1]*A[1] + A[2]*A[2])

def main ():
   Astring = input ("Enter vector A:\n")
   Bstring = input ("Enter vector B:\n")

   A = list(map (int, Astring.split (" "))) #this splits the argument A into words and maps it to the list. 
   B = list(map (int, Bstring.split (" "))) #this splits the argument B into words and maps it to the list.

   print ("A+B =",vector_sum (A, B))
   print ("A.B =",vector_product (A, B))
   print ("|A| = {:.2f}".format (vector_norm (A))) #prints the norm of A in a floating point decimal with 2 decimal places
   print ("|B| = {:.2f}".format (vector_norm (B))) #prints the norm of B in a floating point decimal with 2 decimal places

if __name__ == "__main__":
   main ()
   