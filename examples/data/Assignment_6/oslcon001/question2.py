# basic vector calculations
# Conor O'Sullivan
# 22/04/2014


import math
#Enter vectors
def main():
       VecA = input("Enter vector A:\n")
       VecA = VecA.split()
       VecB = input("Enter vector B:\n")
       VecB = VecB.split()
       add(VecA, VecB)
       dot(VecA, VecB)
       normA(VecA)
       normB(VecB)
       

#Addition of vectors
def add(A,B):
       add_list = []
       for x in range(len(A)):
              add = int(A[x]) + int(B[x])

              add_list.append(add)
       print("A+B =",add_list)
       
#dot product of vectors
def dot(A,B):
       dot = 0
       for x in range(len(A)):
              multi = int(A[x]) * int(B[x])
              dot += multi
       print ("A.B =",dot)
       
#Norm A
def normA(A):
       add = 0
       for x in range(len(A)):
              power = int(A[x])**2
              add += power
       add = "{0:0.2f}".format(math.sqrt(add))
       print ("|A| =",add)       

#Norm B
def normB(B):
       add = 0
       for x in range(len(B)):
              power = int(B[x])**2
              add += power
       add = "{0:0.2f}".format(math.sqrt(add))
       print ("|B| =",add)       

       
main()