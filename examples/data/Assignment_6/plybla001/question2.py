"""Vector operations
B.Player
20/04/2014"""

import math

#initialising of globals
A,B =[],[]

def fill_lists():
   """"Fills arrays with vectors"""
   elementsA = input("Enter vector A:\n").split()
   elementsB = input("Enter vector B:\n").split()
   for element in elementsA:      
      A.append(eval(element))
   for element in elementsB:      
      B.append(eval(element))    
     
   
def addition():
   """vector addition"""
   a=A[0]+B[0]
   b=A[1]+B[1]
   c=A[2]+B[2]
   print("A+B = [",a,", ",b,", ",c,"]",sep='')

def multiplication():
   """dot multiplication"""
   a=A[0]*B[0]
   b=A[1]*B[1]
   c=A[2]*B[2]
   print("A.B =",a+b+c)

def normalise():
   """Noramlises vectors"""
   a = math.sqrt(A[0]**2+A[1]**2+A[2]**2)
   b = math.sqrt(B[0]**2+B[1]**2+B[2]**2)
   print("|A| = {0:.2f}\n|B| = {1:.2f}".format(a,b))
   
def main():
   fill_lists()
   addition()
   multiplication()
   normalise()

main()