"""User enters values for two different vetors, program then performs calculations
Chris Bolton """

from math import *

a = input("Enter vector A:\n")
b = input("Enter vector B:\n")

list_A = list(a.split(" ")) #create lists, enters values seperated by spaces
list_B = list(b.split(" "))

add = [int(list_A[0])+int(list_B[0]),int(list_A[1])+int(list_B[1]),int(list_A[2])+int(list_B[2])] #addition calculations
dot = int(list_A[0])*int(list_B[0])+int(list_A[1])*int(list_B[1])+int(list_A[2])*int(list_B[2])
normA = round(sqrt(int(list_A[0])**2+int(list_A[1])**2+int(list_A[2])**2),2)
normB = round(sqrt(int(list_B[0])**2+int(list_B[1])**2+int(list_B[2])**2),2)

print ("A+B =", add)
print ("A.B =", dot)
print ("|A| = %.2f" % normA)
print ("|B| = %.2f" % normB)