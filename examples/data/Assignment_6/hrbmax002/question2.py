from math import *

a = input("Enter vector A:\n")
b = input("Enter vector B:\n")

listA = list(a.split(" "))
listB = list(b.split(" "))

add = [int(listA[0])+int(listB[0]),int(listA[1])+int(listB[1]),int(listA[2])+int(listB[2])]
dot = int(listA[0])*int(listB[0])+int(listA[1])*int(listB[1])+int(listA[2])*int(listB[2])
normA = round(sqrt(int(listA[0])**2+int(listA[1])**2+int(listA[2])**2),2)
normB = round(sqrt(int(listB[0])**2+int(listB[1])**2+int(listB[2])**2),2)

print ("A+B =", add)
print ("A.B =", dot)
print ("|A| = %.2f" % normA)
print ("|B| = %.2f" % normB)

