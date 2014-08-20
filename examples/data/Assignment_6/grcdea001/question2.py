"""Assignment 6, question 2:performs basic vector addition, dot product and normalisation
Dean Gracey
20 April 2014"""
import math
a = input("Enter vector A:\n")
b = input("Enter vector B:\n")

a = a.split(" ")
b = b.split(" ")
addition = []

#Addition
for i in range(0,3):
    addition.append(int(a[i]) + int(b[i]))


print("A+B =", addition)

#multiplication

multi = []
for i in range(0,len(a)):
    multi.append(int(a[i]) * int(b[i]))
    
total = 0  
for i in range(len(multi)):
    total+=multi[i]
print("A.B =", total)

#normalisation
normal = 0
for i in range(0,len(a)):
    normal+= (int(a[i])**2)
normal = math.sqrt(normal)

print("|A| =", "{0:.2f}".format(normal))

normalb = 0
for i in range(0,len(b)):
    normalb+= (int(b[i])**2)
normalb = math.sqrt(normalb)

print("|B| =", "{0:.2f}".format(normalb))